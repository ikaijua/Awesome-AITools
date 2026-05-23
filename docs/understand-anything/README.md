# Understand Anything Introduction

## What is Understand Anything?

**Understand Anything** is an AI-powered codebase and knowledge base analysis tool that transforms complex projects into interactive, visual knowledge graphs. It is designed to help developers quickly grasp large or unfamiliar codebases by providing a "big picture" view through an interactive dashboard.

## Core Philosophy

### Visualization for Clarity
Traditional code reading is linear and overwhelming. Understand Anything builds a graph of files, functions, classes, and dependencies, making relationships explicit and easy to navigate.

### Multi-Agent Intelligence
The system employs a pipeline of specialized agents (Project Scanner, File Analyzer, Architecture Analyzer, etc.) to autonomously extract logic, business domains, and architectural patterns.

### Context Management
It serves as a critical bridge between raw code and AI agents, providing high-level context that reduces token usage and improves the accuracy of AI coding assistants.

## Core Features

### Interactive Knowledge Graph
- **Visual Navigation:** Clickable nodes representing files, functions, and classes.
- **Dependency Mapping:** Visualizes how different parts of the system interact.

### Architecture Guided Tours
- **Logical Sequence:** Automatically generates walkthroughs of the architecture ordered by dependency.
- **Step-by-Step Learning:** Teaches you the codebase in a logical, structured way.

### Multi-Platform Integration
- **Plugin Support:** Native plugin for Claude Code.
- **Broad Compatibility:** Works with Cursor, VS Code (GitHub Copilot), Cline, and more as a skill or auto-discovered plugin.

### Advanced Analysis
- **Domain View:** Maps code to real-world business processes and flows.
- **Diff Impact Analysis:** Predicts how proposed changes will ripple through the system.
- **Semantic Search:** Ask natural language questions about the codebase structure.

## Quick Start

### Installation

Understand Anything can be installed as a global CLI tool or integrated into your favorite AI agent.

```bash
npm install -g understand-anything
```

### Basic Usage

1. **Scan Project:** Run the scanner to build the knowledge graph.
   ```bash
   understand scan .
   ```
2. **Open Dashboard:** Launch the interactive visualization.
   ```bash
   understand dashboard
   ```
3. **Claude Code Integration:** Use the plugin directly within Claude Code.
   ```bash
   /understand "How does the auth flow work?"
   ```

## Related Resources

- [GitHub Repository](https://github.com/Lum1104/Understand-Anything)
- [Official Website](https://understandanything.ai)

## License

Understand Anything is open-source and available under the MIT License.
