#!/usr/bin/env python3
"""
anti-slop validator

Scans a text for patterns commonly associated with generic AI-generated prose,
in English and/or Spanish. This is a deterministic linter, not a judgment of
quality -- it flags candidate issues with line numbers and context so a human
(or Claude) can decide what to actually fix.

Usage:
    python validate.py <file> [--lang en|es|auto] [--threshold N] [--json]
    echo "some text" | python validate.py - --lang auto

Exit code: 0 if score <= threshold, 1 otherwise. Threshold defaults to 8.
"""

import argparse
import json
import re
import statistics
import sys
from dataclasses import dataclass, field


@dataclass
class Finding:
    category: str
    severity: str  # "low" | "medium" | "high"
    line: int
    snippet: str
    detail: str
    weight: float


# ---------------------------------------------------------------------------
# Phrase banks
# ---------------------------------------------------------------------------

PHRASES_ES = [
    (r"\bno es .{2,40}?,\s*es\b", "high", "Fórmula de contraste 'no es A, es B'"),
    (r"\bno se trata (solo|solamente|únicamente)? ?de\b", "medium", "Fórmula 'no se trata de A'"),
    (r"\bno solo\b.{0,40}\bsino\b", "medium", "Fórmula 'no solo A, sino también B'"),
    (r"\ben (pocas palabras|resumen|conclusi[oó]n)\b", "high", "Cierre redondo de resumen"),
    (r"\blo importante (aqu[ií])? ?es\b", "medium", "Frase de énfasis genérico"),
    (r"\bla clave (est[aá]|es)\b", "medium", "Frase de énfasis genérico"),
    (r"\bvale la pena (destacar|mencionar|se[ñn]alar)\b", "medium", "Muletilla de énfasis"),
    (r"\bcabe (destacar|mencionar|se[ñn]alar)\b", "medium", "Muletilla de énfasis"),
    (r"\bes importante (mencionar|destacar|se[ñn]alar|notar)\b", "medium", "Muletilla de énfasis"),
    (r"\bdicho de otro modo\b", "low", "Reformulación redundante"),
    (r"\bsi pensamos en esto como\b", "low", "Metáfora de manual"),
    (r"\bguía definitiva\b", "medium", "Tono 'guía definitiva'"),
    (r"\bchecklist r[aá]pido\b", "low", "Tono de listículo"),
    (r"^\s*#+\s*¿", "medium", "Subtítulo en forma de pregunta"),
    (r"¿(c[oó]mo funciona|por qu[eé]|en qu[eé] se basa)[^?]{0,60}\?", "medium", "Subtítulo/pregunta tipo FAQ"),
]

PHRASES_EN = [
    (r"\b(it'?s|isn'?t|this isn'?t)\b.{0,40}?[—–]\s*(it'?s|this is)\b", "high", "'It's not A — it's B' contrast"),
    (r"\bis not\b.{2,40}?,\s*(it is|it'?s)\b", "high", "'X is not Y, it's Z' contrast"),
    (r"\bnot only\b.{0,40}\bbut\b.{0,15}\balso\b", "medium", "'Not only A, but also B'"),
    (r"\bin (conclusion|summary)\b", "high", "Round summary closer"),
    (r"\boverall,?\b", "medium", "Generic wrap-up opener"),
    (r"\bin other words\b", "low", "Redundant restatement"),
    (r"\bthat said,?\b", "low", "Generic pivot"),
    (r"\bit'?s worth noting that\b", "medium", "Hedge/filler emphasis"),
    (r"\bthe key is\b", "medium", "Generic emphasis phrase"),
    (r"\bwhat matters here is\b", "medium", "Generic emphasis phrase"),
    (r"\bwhen we think about this as a\b", "low", "Manual-style metaphor framing"),
    (r"\bplays a (crucial|vital|significant) role\b", "medium", "Inflated stock phrase"),
]

INFLATED_ES = [
    "crucial", "robusto", "robusta", "multifacético", "multifacética",
    "ecosistema", "impulsar", "potenciar", "optimizar", "framework",
    "empoderar", "sinérgico", "sinérgica", "holístico", "holística",
]

INFLATED_EN = [
    "crucial", "significant", "delve", "delves", "delving", "explore",
    "navigate", "unlock", "robust", "multifaceted", "foster", "fosters",
    "seamless", "tapestry", "testament", "boasts", "elevate", "leverage",
    "game-changing", "landscape",
]

CONNECTORS_ES = [
    "además,", "por otro lado,", "asimismo,", "en ese sentido,",
    "por su parte,", "cabe resaltar,",
]

CONNECTORS_EN = [
    "furthermore,", "moreover,", "additionally,", "in addition,",
]

EM_DASH_ASIDE = re.compile(r"[—–]\s*[^—–.!?]{3,60}?\s*[—–]")


def detect_lang(text: str) -> str:
    es_hits = len(re.findall(r"\b(el|la|los|las|de|que|es|no|se|con|para|una?)\b", text.lower()))
    en_hits = len(re.findall(r"\b(the|and|of|to|is|not|with|for|a|an)\b", text.lower()))
    return "es" if es_hits >= en_hits else "en"


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def context(text: str, start: int, end: int, pad: int = 30) -> str:
    s = max(0, start - pad)
    e = min(len(text), end + pad)
    snippet = text[s:e].replace("\n", " ")
    return f"…{snippet}…"


def scan_phrases(text: str, bank) -> list:
    findings = []
    for pattern, severity, detail in bank:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            findings.append(
                Finding(
                    category="phrase",
                    severity=severity,
                    line=line_of(text, m.start()),
                    snippet=context(text, m.start(), m.end()),
                    detail=detail,
                    weight={"low": 0.5, "medium": 1.0, "high": 2.0}[severity],
                )
            )
    return findings


def scan_inflated_vocab(text: str, words) -> list:
    findings = []
    for w in words:
        for m in re.finditer(rf"\b{re.escape(w)}\b", text, flags=re.IGNORECASE):
            findings.append(
                Finding(
                    category="vocab",
                    severity="low",
                    line=line_of(text, m.start()),
                    snippet=context(text, m.start(), m.end()),
                    detail=f"Vocabulario inflado: '{w}'",
                    weight=0.4,
                )
            )
    return findings


def scan_connectors(text: str, connectors) -> list:
    findings = []
    count = 0
    for c in connectors:
        for m in re.finditer(re.escape(c), text, flags=re.IGNORECASE):
            count += 1
            findings.append(
                Finding(
                    category="connector",
                    severity="low",
                    line=line_of(text, m.start()),
                    snippet=context(text, m.start(), m.end()),
                    detail=f"Conector de transición: '{c}'",
                    weight=0.3,
                )
            )
    if count >= 3:
        # escalate: repeated use is the real signal, not any single instance
        for f in findings:
            if f.category == "connector":
                f.severity = "medium"
                f.weight = 0.8
    return findings


def scan_em_dash_aside(text: str) -> list:
    findings = []
    for m in EM_DASH_ASIDE.finditer(text):
        findings.append(
            Finding(
                category="structure",
                severity="medium",
                line=line_of(text, m.start()),
                snippet=context(text, m.start(), m.end()),
                detail="Em dash usado como aclaración retórica (X — aside — Y)",
                weight=1.0,
            )
        )
    return findings


def scan_bullet_density(text: str) -> list:
    lines = text.splitlines()
    if not lines:
        return []
    bullet_lines = sum(1 for l in lines if re.match(r"^\s*([-*•]|\d+[.)])\s+", l))
    prose_lines = sum(1 for l in lines if l.strip() and not re.match(r"^\s*([-*•]|\d+[.)])\s+", l) and not l.strip().startswith("#"))
    total = bullet_lines + prose_lines
    if total < 6:
        return []
    ratio = bullet_lines / total
    if ratio > 0.6:
        return [
            Finding(
                category="structure",
                severity="medium",
                line=1,
                snippet=f"{bullet_lines} líneas de bullets de {total} líneas de contenido",
                detail=f"Densidad de bullets alta ({ratio:.0%}) — considerar convertir parte a prosa",
                weight=1.5,
            )
        ]
    return []


def scan_sentence_symmetry(text: str) -> list:
    # crude sentence split; good enough for a heuristic signal
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 0]
    lengths = [len(s.split()) for s in sentences if len(s.split()) >= 3]
    if len(lengths) < 6:
        return []
    mean = statistics.mean(lengths)
    stdev = statistics.pstdev(lengths)
    cv = stdev / mean if mean else 0
    if cv < 0.25:
        return [
            Finding(
                category="structure",
                severity="medium",
                line=1,
                snippet=f"media={mean:.1f} palabras, desv.est={stdev:.1f}, cv={cv:.2f}",
                detail="Longitud de oraciones muy uniforme (poca variación natural)",
                weight=1.2,
            )
        ]
    return []


def run(text: str, lang: str) -> list:
    if lang == "auto":
        lang = detect_lang(text)

    findings = []
    if lang == "es":
        findings += scan_phrases(text, PHRASES_ES)
        findings += scan_inflated_vocab(text, INFLATED_ES)
        findings += scan_connectors(text, CONNECTORS_ES)
    else:
        findings += scan_phrases(text, PHRASES_EN)
        findings += scan_inflated_vocab(text, INFLATED_EN)
        findings += scan_connectors(text, CONNECTORS_EN)

    findings += scan_em_dash_aside(text)
    findings += scan_bullet_density(text)
    findings += scan_sentence_symmetry(text)

    findings.sort(key=lambda f: f.line)
    return findings, lang


def main():
    parser = argparse.ArgumentParser(description="Anti-slop style validator (EN/ES)")
    parser.add_argument("path", help="File path, or '-' to read from stdin")
    parser.add_argument("--lang", choices=["en", "es", "auto"], default="auto")
    parser.add_argument("--threshold", type=float, default=8.0, help="Score above which exit code is 1")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
        source_label = "<stdin>"
    else:
        with open(args.path, "r", encoding="utf-8") as f:
            text = f.read()
        source_label = args.path

    findings, lang_used = run(text, args.lang)
    score = round(sum(f.weight for f in findings), 2)

    if args.json:
        payload = {
            "source": source_label,
            "lang": lang_used,
            "score": score,
            "threshold": args.threshold,
            "findings": [f.__dict__ for f in findings],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"anti-slop validator — {source_label} (idioma detectado/usado: {lang_used})")
        print("=" * 70)
        if not findings:
            print("Sin hallazgos. Nada que corregir por regex — sigue usando criterio.")
        else:
            by_sev = {"high": [], "medium": [], "low": []}
            for f in findings:
                by_sev[f.severity].append(f)
            for sev in ("high", "medium", "low"):
                if not by_sev[sev]:
                    continue
                print(f"\n[{sev.upper()}] ({len(by_sev[sev])} hallazgo(s))")
                for f in by_sev[sev]:
                    print(f"  línea {f.line} · {f.detail}")
                    print(f"    {f.snippet}")
        print("\n" + "-" * 70)
        verdict = "revisar antes de entregar" if score > args.threshold else "aceptable"
        print(f"Score: {score} (umbral: {args.threshold}) — {verdict}")

    sys.exit(1 if score > args.threshold else 0)


if __name__ == "__main__":
    main()
