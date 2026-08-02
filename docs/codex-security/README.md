# Codex Security Introduction

## What is Codex Security?

Codex Security is an open-source CLI and TypeScript SDK from OpenAI for finding, validating, and fixing security vulnerabilities in your code.

## Key Features

- **Repository scanning**: Scan local codebases for security vulnerabilities.
- **Finding tracking**: Track findings across multiple runs and compare scan results.
- **Fix verification**: Validate that a fix actually resolves the underlying issue.
- **CI/CD integration**: Run non-interactive scans in pipelines using `OPENAI_API_KEY` or `CODEX_API_KEY`.
- **TypeScript SDK**: Embed scanning capabilities directly into Node.js applications.
- **Containerized bulk scans**: Use the official Docker image for scalable, resumable scans.

## Quick Start

```bash
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
```

For CI environments:

```bash
export OPENAI_API_KEY=sk-...
npx @openai/codex-security scan .
```

## Links

- [GitHub Repository](https://github.com/openai/codex-security)
- [OpenAI Codex Security Documentation](https://github.com/openai/codex-security/tree/main/docs)
