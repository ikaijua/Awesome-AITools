# Pi Introduction

## What is Pi?

Pi is an open-source (MIT) agent harness and self-extensible coding agent from [earendil-works](https://github.com/earendil-works). It is designed as a modular TypeScript/Bun monorepo where the model provides the "brain" and Pi provides the "body" — tool calling, state management, UI, and execution.

The project is best known for its interactive terminal coding agent, but it also publishes reusable packages for building other kinds of agents.

## Core Packages

| Package | Description |
| --- | --- |
| `@earendil-works/pi-coding-agent` | Interactive coding agent CLI |
| `@earendil-works/pi-agent-core` | Agent runtime with tool calling and state management |
| `@earendil-works/pi-ai` | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| `@earendil-works/pi-telemetry` | Vendor-neutral telemetry contracts and conformance tests |
| `@earendil-works/pi-tui` | Terminal UI library with differential rendering |

## Core Philosophy

### Self-extensible agent
Everything in Pi is intended to be replaceable: the model, the tools, the interface, and the approval policy. The default coding agent is a starting point rather than a closed product.

### Supply-chain hardening
Pi treats dependency changes as reviewed code changes:
- Direct dependencies are pinned to exact versions
- `package-lock.json` is the ground truth and pre-commit hooks block accidental changes
- Published CLI includes `npm-shrinkwrap.json` to pin transitive dependencies
- CI runs `npm audit --omit=dev` and signature verification

### Sandboxing options
Pi has no built-in permission system by default, but documents three containment patterns:
- **Gondolin extension**: keep Pi and provider auth on the host while routing built-in tools and `!` commands into a local Linux micro-VM
- **Plain Docker**: run the whole `pi` process in a local container
- **OpenShell**: run Pi inside a policy-controlled sandbox

## Quick Start

Install dependencies without running lifecycle scripts:

```sh
npm install --ignore-scripts
npm run build
./pi-test.sh   # run pi from source
```

Standalone binaries can be built from a release source archive:

```sh
VERSION="<release-version>"
tar -xzf "pi-${VERSION}-source.tar.gz"
cd "pi-${VERSION}"
./scripts/build-binaries.sh --offline-model-data --platform linux-x64 --out "$PWD/out"
```

## Notes

- New issues and PRs from new contributors are auto-closed by default; maintainers review them daily.
- For chat automation and workflow use cases, see the related [`earendil-works/pi-chat`](https://github.com/earendil-works/pi-chat) repository.
- A popular fork is [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi), which adds IDE-style features such as LSP, DAP debugging, and Python/Bun code execution.

## Related Resources

- [GitHub Repository](https://github.com/earendil-works/pi)
- [Project Website](https://pi.dev)
- [Pi Chat](https://github.com/earendil-works/pi-chat)
- [oh-my-pi fork](https://github.com/can1357/oh-my-pi)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Pi is released under the MIT License.
