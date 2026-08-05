# QM Introduction

## What is QM?

[QM](https://github.com/yc-software/qm) is an open-source **multi-agent harness for organizations**, built by Y Combinator. It runs on Slack and the Web and is designed to organize agents around company structure rather than act as a personal assistant.

The central design concept is the **scope**: every employee, project, and channel gets an isolated workspace containing its own memory, files, credentials, permissions, and scheduled tasks. Agents operate within the scope of the people and teams they serve, using those identities and permissions, so access control follows real organizational boundaries.

## Core Positioning

### From Personal Assistants to Organizational Agents
YC arrived at QM after three earlier iterations — a basic agent loop, cron/webhook triggers, and OpenClaw/Hermes agents — because managing dozens of agents at a company became unwieldy. QM treats the organization itself as the unit of coordination.

### Scope-Based Isolation
Each scope is a self-contained unit: memory, files, credentials, permissions, and cron jobs stay tied to a person, project, or channel. This prevents the "super-agent with all permissions" problem and makes actions auditable.

### Headless, Replaceable Core
QM's architecture separates the headless core (API, identity, policy, scheduling) from the Web UI and Slack client. PostgreSQL provides persistence, and both the model provider and the agent harness are swappable, so teams are not locked into a single vendor.

## Core Features

- **Scope-based workspaces** — isolated memory, files, credentials, and permissions per employee/project/channel.
- **Slack and Web clients** — interact with agents where teams already work.
- **Headless core** — API-first design with pluggable UI and chat interfaces.
- **Agent identity mirroring** — agents act as the people they serve, inheriting credentials and permissions.
- **Auditability** — all agent actions are traceable and scoped.
- **Self-hostable** — deploy via Docker, Fly.io, or AWS.
- **Human-readable contributions** — accepts human-written `.txt` / `.md` contributions instead of direct code patches.

## Quick Start

### Prerequisites
- Node.js and pnpm
- PostgreSQL
- A Slack workspace (optional, for Slack integration)

### Install and run locally

```bash
git clone https://github.com/yc-software/qm.git
cd qm
# Follow the setup instructions in the repository README
pnpm install
pnpm dev
```

### Deploy with Docker

```bash
# Use the provided Dockerfile and compose configuration in the repository
docker build -t qm .
docker run -e DATABASE_URL=postgres://... qm
```

## Best Practices

1. **Scope agents tightly** — create separate scopes for teams, projects, and sensitive functions.
2. **Mirror real permissions** — let agents use the credentials of the person they serve instead of shared super-credentials.
3. **Review audit logs** — regularly check what agents did and on whose behalf.
4. **Start with low-risk workflows** — automate reporting, summaries, and notifications before handing off write access.
5. **Self-host for sensitive data** — keep company data and credentials inside your own infrastructure.

## Security Notice

QM is early experimental software. The project transparently lists known limitations (for example, command policies that can be bypassed, sandbox credentials stored in plaintext). Review the repository's security documentation before deploying to production or granting access to sensitive systems.

## Related Resources

- [GitHub Repository](https://github.com/yc-software/qm)
- [Y Combinator](https://www.ycombinator.com/)
- [OpenClaw](https://github.com/openclaw/openclaw) — one of the harnesses QM evolved from
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — another agent framework in the QM ecosystem

## License

QM is released under the license specified in its [GitHub repository](https://github.com/yc-software/qm).
