# AGENTS.md: A "Project README" for AI Coding Agents

As more teams introduce coding agents like Cursor, Aider, VS Code AI plugins, Devin, and Windsurf into their daily development, a practical problem has emerged: Agents need stable, clear, and machine-readable project context. However, common `README.md` files are often "written for humans"—they introduce the product, write contribution guides, and cram in build/test/format commands, ending up long and messy. Agents trying to find key operation steps in such documents can easily miss, misunderstand, or go astray.

`AGENTS.md` was born for this: it provides a simple, open convention—placing a Markdown file named `AGENTS.md` in the repository, specifically for "project descriptions for AI coding agents." You can think of it as:

- **A README for coding agents:** Focuses only on context, commands, rules, paths, and constraints; no marketing, no long-form human narratives.
- **Project Homepage:** https://agents.md/

## What problem does it solve?

### 1. Free "Human README" from the instruction swamp
- `README.md` needs to face newcomers, human contributors, and product users.
- Agents need executable details: how to install dependencies, run tests, where to change after generating code, and how to interpret CI failures.

### 2. Provide a certain, predictable "entry file" for Agents
- Instead of letting Agents guess whether it's `CONTRIBUTING.md` or `docs/dev.md`, just agree: look at `AGENTS.md`.

### 3. Support "local effect" in large repositories/Monorepos
- `AGENTS.md` supports nested files in subdirectories.
- Agents should read the `AGENTS.md` closest to the current file, allowing different sub-projects to have their own build commands and specifications.

## Core Design: Simple, Open, Layered

### 1. Open Format: Just Markdown
`AGENTS.md` does not introduce a proprietary DSL or force a field structure—you write standard Markdown. This means:
- Both humans and machines can read it;
- Existing documentation systems don't need major changes;
- You can evolve it according to your team's habits.

### 2. Layers/Priority: Closer is more effective
In Monorepos or multi-module projects, you can organize it like this:
- `/AGENTS.md` (Global constraints: common commands, common specifications)
- `/packages/foo/AGENTS.md` (Foo sub-project: its own dev/test/build methods)

Priority principles:
- The `AGENTS.md` closest to the target file/directory has the highest priority;
- Instructions manually entered by the user in the dialog box have higher priority (i.e., "chat prompts" override documents).

### 3. Wide Compatibility: For various agent tools
Compatible tools listed on the project homepage include (but are not limited to): Cursor, Aider, VS Code, Devin, Windsurf, and other mainstream AI coding agents/IDE toolchains.

## Quick Start: 3 minutes to get Agents on track

`AGENTS.md` doesn't require any software installation:
1. Create a file in the repository root: `AGENTS.md`
2. Write what the Agent really needs (commands, paths, rules, boundary conditions)

A practical starting template:
```markdown
## Setup commands
- Install deps: `pnpm install`
- Start dev server: `pnpm dev`
- Run tests: `pnpm test`

## Code style
- TypeScript strict mode
- Single quotes, no semicolons
```

It's recommended to supplement these high-value categories:
- **Project Structure Map:** Key directories, core modules, entry files.
- **CI/Test Matrix:** Unit/integration test commands, coverage, time estimates.
- **Change Strategy:** Which files must be updated when a certain module changes, APIs that must not be broken.
- **Validation after code generation:** Minimum loop for lint/format/test.
- **Security & Permission Boundaries:** Untouchable secrets/production configs, dangerous operation bans.

## What should be written in AGENTS.md? Are there "required fields"?
Conclusion: `AGENTS.md` has no mandatory fields or official "required questions." it just agrees on a filename and format (Markdown). The content is entirely up to you. To make Agent behavior more stable and controllable, it's recommended to write it as an "executable operation manual."

## References
- AGENTS.md Project Homepage: https://agents.md/
- Agentic AI Foundation: https://aaif.io/
