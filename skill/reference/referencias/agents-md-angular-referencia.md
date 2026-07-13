# Referencia — AGENTS.md de proyecto Angular (ng-adagestor)

Texto completo tal como lo pegó el usuario, de otro proyecto ADA (Angular 20 + Boreal Design System). Referencia base para la sección de reglas de trabajo, estructura de proyecto, testing y disciplina de contexto en [02-agents-claude-md-canon.md](../02-agents-claude-md-canon.md).

---

# Repository Guidelines

This is an ADA development project. Act as a technical coding assistant: ship maintainable changes that fit the existing Angular 20 system, the product context, and the Boreal Design System direction.

## Working Rules

- Read the relevant code before editing.
- Prefer the smallest useful change that solves the request.
- Apply KISS/DRY: keep solutions simple, avoid repetition, and only abstract when it clearly removes real duplication or complexity.
- Reuse existing patterns, components, services, modules, utilities, tokens, and test style.
- Challenge fragile assumptions, risky shortcuts, and unnecessary abstractions.
- Do not add dependencies, change public contracts, or cross module boundaries without checking impact.
- Keep business rules out of UI components when a domain service, model, or feature layer is the better place for them.
- Keep diffs focused; do not mix feature work with cosmetic cleanup.
- Do not revert changes you did not make.
- Do not run destructive commands without explicit approval.
- Use the `/delegation` plugin early and often for non-trivial work. Delegate at least one bounded, safe slice whenever possible, such as repo inventory, multi-file audit, repetitive edits, independent review, or verification. Keep tiny, ambiguous, security-sensitive, and high-judgment tasks in the main context.

## Project Structure & Module Organization

This is an Angular 20 application named `ng-adagestor`. Application code lives in `src/app`, with top-level areas for `auth`, `core`, `layout`, `models`, `pages`, `services`, `shared`, and `util`. Environment files are in `src/environments`, global styles start at `src/styles.scss`, and theme assets live under `src/theme`. Static assets are served from `public`, including PrimeNG styling in `public/css/components-prime-ng.scss`. Build output goes to `dist/ng-adagestor`. Deployment files live at the root, including `Dockerfile`, `default.conf`, and Kubernetes YAML files.

`src/app/shared` is being deprecated for new reusable UI work. Do not add new cross-feature components there. New project-level reusable components should live under `src/app/core/components/<component-name>/`, with the component, spec, styles/templates if split, and any local documentation grouped in that folder. Feature-only components should remain inside their owning feature folder.

Current major feature areas include authentication, the task dashboard and task views, account management, and administrator management pages under `src/app/pages/administrador` for users, spaces, teams, states, reports, task upload, novelty, projects, and milestones. Routes are standalone/lazy-loaded in `src/app/app.routes.ts`, with `authGuard` and `adminGuard` protecting private and management areas.

Project documentation lives in `docs/`, with backend/domain references under `docs/backend`. Visual direction for BDS/SicofERP work is summarized in `DESIGN.md`; consult it before making meaningful UI changes.
Use the root INDEX.md as the first navigation map for the repo; it points to the exact files and folders to inspect before opening broad context.

## Core Components & BDS Readiness

Components under `src/app/core/components` are project-level UI building blocks and should be ready to evolve into Boreal Design System (BDS) components when appropriate. Keep them generic, documented, and independent from a specific page or business flow.

Existing core components include `expressive-list-item`, `operation-feedback-dialog`, and `user-invitation-dialog`. Reuse or extend these before creating a similar component elsewhere.

For each new core component:

- Create a dedicated folder: `src/app/core/components/<component-name>/`.
- Use standalone Angular components and explicit imports.
- Define a small, typed public API with exported interfaces/types for inputs, dialog data, or action results.
- Document intent, usage examples, configurable inputs/data, emitted events/results, and known constraints in code comments or a local README when the component has more than a trivial API.
- Use BDS components from `@ada-lib/ui-kit` first, and use Material/BDS design tokens such as `--mat-sys-*` for color, surface, typography, and elevation.
- Avoid page-specific copy, API details, route assumptions, or feature state inside the reusable component.
- Keep visual decisions compatible with BDS: density, accessibility, responsive behavior, keyboard/dialog semantics, and token-based theming.
- Add or update focused specs next to the component.

Any local wrapper around a BDS component, DOM-level adaptation, or styling override that targets a `bds-*` element must be documented. Add a short code comment when the reason is not obvious, and add or update an entry in `docs/bds-local-customizations.md`. Record the local need, affected BDS component, implementation location, constraints, and the proposed change to move into `@ada-lib/ui-kit` later.

## Frontend UX

- Use ADA/Boreal Design System components from `@ada-lib/ui-kit` when available. The repo currently targets `@ada-lib/ui-kit` 7.4.x alongside Angular Material/CDK 20 and PrimeNG 20.
- Build dense, clear, operational interfaces for work tools; avoid marketing or landing-page patterns unless explicitly requested.
- Handle loading, empty, error, disabled, and success states when they affect the user flow.
- Do not nest cards inside cards.
- Treat Figma as a reference, then validate against the real system, available components, and responsive behavior.
- Keep visual changes token-based and compatible with the existing Material/BDS theme.
- Prefer BDS controls for new or redesigned UI. PrimeNG remains present across existing screens; use it where the surrounding feature already depends on it or BDS does not cover the needed control.
- Use Angular 20 control flow (`@if`, `@for`, `@switch`) in templates. Do not introduce new `*ngIf` or `*ngFor` usage.
- Prefer Angular signals (`signal`, `computed`, `input`, `output`, `model`) for local reactive state when that matches nearby code.
- Use `@ngx-translate` patterns already configured in `src/app/app.config.ts` for translated copy.
- Use FullCalendar only in calendar/task-view contexts where the existing feature pattern already applies.

## Build, Test, and Development Commands

Use the package scripts in `package.json`:

- `npm start` or `bun run start`: run the Angular dev server.
- The user normally keeps `localhost:4200` open for live preview. Do not start another dev server or run a build unless it is strictly necessary for the requested work or verification.
- `npm run build`: build the default production bundle.
- `npm run build:dev`: build with `src/environments/environment.dev.ts`.
- `npm run build:qa`: build with the QA environment replacement; verify the configured replacement file exists before relying on it.
- `npm run build:prod`: production AOT build with extra Node memory.
- `npm test`: run Karma/Jasmine unit tests.
- `npm run watch`: rebuild continuously for local development.
- `npm run release`: run `standard-version` for changelog and version updates.

## Coding Style & Naming Conventions

Follow `.editorconfig`: UTF-8, 2-space indentation, final newline, and trimmed trailing whitespace. TypeScript files use single quotes. Angular schematics default to standalone components, directives, and pipes with SCSS styles. Keep files grouped by feature and use Angular naming patterns such as `feature-name.component.ts`, `feature-name.service.ts`, and `feature-name.pipe.ts`. Prefer existing feature-local helpers or `src/app/core/components` for reusable UI instead of adding new code to deprecated `src/app/shared`.

Preserve text encoding exactly. All project files must remain valid UTF-8: when editing files with Spanish copy, accents, `ñ`, punctuation, or symbols, read and write them as UTF-8 and do not replace them with mojibake such as `Ã`, `Â`, or `�`. Before finishing any change that touches user-facing copy, run a targeted search for those mojibake markers in the edited files and fix them instead of converting Spanish text to ASCII.

Use explicit standalone imports in components. Keep route-level code lazy-loaded when adding pages. Avoid enabling broad schemas such as `CUSTOM_ELEMENTS_SCHEMA` to hide component integration errors.

## Testing Guidelines

Unit tests use Jasmine with Karma via Angular CLI. Place specs beside the code they cover using `*.spec.ts`, as in `src/app/app.component.spec.ts`. Run `npm test` before submitting changes that touch components, services, routing, or shared behavior. Add focused tests for new business logic and regressions.

Verification expectations:

- Bugfix: reproduce first, fix second, verify last.
- Logic change: add or run a focused test.
- Shared behavior: run related tests; run a build only when strictly necessary or when the change can reasonably affect compilation/bundling.
- API or contract change: check consumers and `openapi.yaml` when relevant.
- Visual change: inspect manually on the existing `localhost:4200` session or with a screenshot when useful.
- Do not use browser-based verification or manual navigation as a default check. Avoid opening a browser or running login-dependent flows unless the user explicitly asks for it or there is no other practical way to verify; these sessions usually require authentication and waste tokens unnecessarily.
- If verification cannot be run, say so clearly and explain the remaining risk.

## Commit & Pull Request Guidelines

Recent history uses Conventional Commit-style messages such as `feat: ...` and `fix(auth): ...`, mixed with GitLab merge commits. Prefer concise subjects: `feat(scope): summary`, `fix(scope): summary`, or `refactor(scope): summary`. Pull requests should include a short description, linked issue or ticket, testing notes, and screenshots or recordings for visible UI changes. Call out environment, deployment, or API contract changes explicitly.

Final assistant responses for code changes should state what changed, relevant files, verification performed, and any risks or follow-ups. Do not claim completion without verification.

## Configuration & Security

Do not commit secrets or local credentials. Keep environment-specific values in the appropriate `src/environments` file and verify file replacements in `angular.json` when adding new build targets. Treat `openapi.yaml` as the source reference for API contract changes.

## Token Discipline

- Start with the smallest relevant context.
- Read files before editing.
- Grep callers before changing shared functions.
- Prefer exact file and line references over broad re-reads.
- Stop after the first working patch and ask before widening scope.
- Keep shell output short; prefer targeted commands over whole-file dumps.

---

## Qué se toma de aquí para el canon

- La estructura completa de secciones (Working Rules → Project Structure → UX/dominio → Commands → Coding Style → Testing → Commit/PR → Configuration & Security → Token Discipline).
- El patrón de "Verification expectations" por tipo de cambio (bugfix, lógica, contrato, visual).
- "Token Discipline" se adapta como "Disciplina de contexto" en el canon.
- La sección de `/delegation` **no se hereda** — el usuario está dando de baja esa skill por malos resultados.
