# Grok Build Introduction

## What is Grok Build?

Grok Build (the `grok` CLI/TUI) is xAI's terminal-based AI coding agent. It runs as a full-screen, mouse-interactive TUI that understands your codebase, edits files, executes shell commands, searches the web, and manages long-running tasks. It can be used interactively, headlessly for scripting/CI, or embedded in editors via the Agent Client Protocol (ACP).

The project is open source (Apache-2.0), written in Rust, and periodically synced from the SpaceXAI monorepo. A `SOURCE_REV` file at the repository root records the exact monorepo commit the tree was built from.

## Core Philosophy

### Terminal-first coding agent
Grok Build is built for developers who want to stay in the terminal:
- Launch a full-screen TUI directly in a project directory
- Ask natural-language questions about a repository
- Let the agent plan, edit files, run tools, and iterate in the same session

### Multiple run modes
- **Interactive TUI** — scrollback, prompt, modals, mouse interaction
- **Headless mode** — non-interactive runs for scripting and CI
- **ACP integration** — embed the agent in ACP-compatible editors

### Extensible agent runtime
Grok Build ships the capabilities commonly needed for agentic development:
- MCP servers
- Skills and plugins
- Lifecycle hooks
- Sandboxing and workspace checkpoints
- Theming and configuration

## Core Features

### Code understanding and editing
- Analyze project structure and dependencies
- Read, search, and modify files
- Implement features, fix bugs, and refactor code

### Shell and workflow automation
- Run build, test, lint, and project scripts
- Chain multiple steps while observing tool feedback
- Manage long-running tasks

### Web and integrations
- Search the web from within a session
- Configure MCP servers, skills, plugins, and hooks

## Quick Start

### Installing the released binary

Prebuilt binaries are published for macOS, Linux, and Windows:

```sh
curl -fsSL https://x.ai/cli/install.sh | bash   # macOS / Linux / Git Bash
irm https://x.ai/cli/install.ps1 | iex          # Windows PowerShell
grok --version
```

On first launch it opens your browser to authenticate.

### Building from source

Requirements:
- **Rust** — the toolchain is pinned by `rust-toolchain.toml`; `rustup` installs it automatically on first build.
- **[DotSlash](https://dotslash-cli.com)** — required so hermetic tools under `bin/` (notably `bin/protoc`) can download and run.
- **protoc** — proto codegen resolves `bin/protoc` via DotSlash, or falls back to a `protoc` on `PATH` / `$PROTOC`.
- macOS and Linux are supported build hosts; Windows builds are best-effort.

```sh
cargo run -p xai-grok-pager-bin              # build + launch the TUI
cargo build -p xai-grok-pager-bin --release  # release binary: target/release/xai-grok-pager
cargo check -p xai-grok-pager-bin            # fast validation
```

The binary artifact is named `xai-grok-pager`; official installs ship it as `grok`.

## Repository Layout

| Path | Contents |
| --- | --- |
| `crates/codegen/xai-grok-pager-bin` | Composition-root package; builds the `xai-grok-pager` binary |
| `crates/codegen/xai-grok-pager` | The TUI: scrollback, prompt, modals, rendering |
| `crates/codegen/xai-grok-shell` | Agent runtime + leader/stdio/headless entry points |
| `crates/codegen/xai-grok-tools` | Tool implementations (terminal, file edit, search, ...) |
| `crates/codegen/xai-grok-workspace` | Host filesystem, VCS, execution, checkpoints |
| `third_party/` | Vendored upstream source (Mermaid diagram stack) |

## Notes

- **External contributions are not accepted** (see `CONTRIBUTING.md` in the repository).
- The root `Cargo.toml` is generated — treat it as read-only and prefer editing per-crate `Cargo.toml` files.

## Related Resources

- [GitHub Repository](https://github.com/xai-org/grok-build)
- [Official Documentation](https://docs.x.ai/build/overview)
- [Grok Build homepage](https://x.ai/cli)
- [Changelog](https://x.ai/build/changelog)
- [Comparison with Other Tools](../COMPARISON.md)

## License

First-party code in the repository is licensed under the Apache License, Version 2.0. Third-party and vendored code remains under its original licenses.
