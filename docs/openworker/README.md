# OpenWorker Introduction

## What is OpenWorker?

OpenWorker is an open-source, local-first desktop AI coworker released by Andrew Ng. Instead of returning chat replies, it carries everyday tasks through to completion—drafting documents, sending Slack replies, updating calendars, triaging inboxes, and producing polished deliverables. It runs on your own machine, connects to the tools where your work already happens, and lets you bring your own model.

## Core Philosophy

### Outcome-First Delegation
Ask for a finished result—"prepare the Monday brief," "draft a customer follow-up," "untangle my calendar"—and OpenWorker breaks it into steps, works across connected tools, and returns a deliverable you can use.

### Local-First Privacy
The agent loop, conversations, connector tokens, and model keys live on your device. Data leaves your machine only through the model and integrations you choose.

### Model Independence
No vendor lock-in. Use cloud providers, open-weight models, or fully local inference via Ollama. Switch models per task if needed.

## Core Features

### Real Deliverables
Produces documents, spreadsheets, reports, web pages, and message drafts as finished artifacts—not to-do lists or draft dumps.

### 25+ Tool Integrations
Connects to Slack, Gmail, Outlook, Google Calendar, Notion, HubSpot, GitHub, Jira, Linear, Asana, Dropbox, and more. Any MCP-accessible tool can also be added with per-tool access control.

### Approval Before Consequential Actions
Before sending a message, changing a calendar, writing a file, or running a shell command, OpenWorker checks in and waits for your approval.

### Recurring Automations
Schedule recurring tasks such as morning briefs, weekly reports, inbox checks, and channel monitoring.

### Slack Integration
Mention `@OpenWorker` in a Slack channel to open a desktop session; the result is posted back as a thread reply.

## Quick Start

### Download Prebuilt App

Visit [openworker.com](https://openworker.com) to download the macOS (Apple Silicon) or Windows (x64) desktop app.

### Run from Source

```bash
git clone https://github.com/andrewyng/openworker
cd openworker

# One-time bootstrap (creates .venv)
bash packaging/setup_dev_env.sh

# Start the local agent server
.venv/bin/openworker-server --cwd ~/some/project --port 8765

# In a second terminal, start the UI
cd surfaces/gui
npm install
npm run dev
```

For the full desktop app, replace the last step with `npm run tauri dev`.

## Best Practices

1. **Ask for outcomes, not steps** - Describe the deliverable you want rather than micromanaging the workflow.
2. **Start with limited permissions** - Approve tool access gradually as you build trust.
3. **Review check-ins** - Consequential actions are gated; use them to stay in control.
4. **Use local models for sensitive work** - Ollama support keeps data fully on-device.

## Related Resources

- [GitHub Repository](https://github.com/andrewyng/openworker)
- [Official Website](https://openworker.com)
- [Issues & Discussions](https://github.com/andrewyng/openworker/issues)

## License

OpenWorker is released under the MIT license. Please follow its open-source license when using it.
