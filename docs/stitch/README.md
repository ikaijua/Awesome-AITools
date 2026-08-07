# Stitch Introduction

## What is Stitch?

[Stitch](https://stitch.withgoogle.com/) is an experimental **AI-powered UI design tool** from Google Labs. It turns text prompts, sketches, or voice descriptions into high-fidelity interface prototypes and frontend code, bridging the gap between design thinking and production-ready UI.

Stitch is built around the idea of **"vibe design"** — you describe the feeling or goal of an interface, and the tool generates visual layouts, design systems, and interactive flows. It can export designs to Figma or output HTML/CSS code for further development.

## Core Positioning

### Design for the Agentic Era
Stitch is designed to work alongside AI coding agents. It offers an SDK and MCP server so that agents like Claude Code, Cursor, and Gemini CLI can pull design tokens, components, and prototypes programmatically. This connects vibe design directly with vibe coding.

### From Prompt to Interactive Prototype
Instead of starting from blank artboards, designers and developers describe what they want users to feel or accomplish. Stitch produces multi-screen prototypes, applies design systems, and lets users iterate via voice or direct manipulation.

### Complement to Existing Tools
Stitch does not replace Figma or Android Studio. It is positioned as a rapid ideation and prototyping layer: generate concepts in Stitch, refine in Figma, and implement in your preferred IDE.

## Core Features

- **Text-to-UI** — generate high-fidelity interfaces from natural-language prompts.
- **Sketch and voice input** — turn hand-drawn sketches or spoken descriptions into layouts.
- **Multi-screen prototypes** — create connected screens and interactive flows.
- **Design system support** — choose from built-in design systems or import your own.
- **Code export** — export generated designs as HTML/CSS or open them in Google AI Studio.
- **Figma integration** — send designs to Figma for detailed refinement.
- **MCP server & SDK** — connect Stitch to coding agents and editor workflows.
- **Real-time steering** — adjust layouts and styles conversationally without rewriting prompts.

## Quick Start

### Use the web app

Visit [stitch.withgoogle.com](https://stitch.withgoogle.com/) and sign in with a Google account.

### Create a design

1. Enter a prompt such as:
   > "Create a dashboard for an education platform where users learn about AI and automation."
2. Stitch generates a multi-screen layout.
3. Iterate via prompt, voice, or direct editing.
4. Export to Figma or copy the generated frontend code.

### Connect to a coding agent

Install the Stitch MCP server and SDK (documented on the official site) to let agents access your design tokens and components directly.

## Best Practices

1. **Start with user goals, not widgets** — describe what users should feel or accomplish, then refine visual details.
2. **Use Figma for final polish** — treat Stitch output as a starting point for detailed design systems.
3. **Lock down design tokens early** — consistent tokens make agent-driven implementation much easier.
4. **Iterate with voice for speed** — voice steering is often faster than rewriting prompts for layout tweaks.
5. **Review generated code before shipping** — like all AI-generated output, exported code should be reviewed and tested.

## Limitations

- Works best for concepts and prototypes rather than production-complete applications.
- Monthly usage quotas apply during the preview.
- English-only access in the current preview.
- Generated results can vary in quality depending on prompt specificity.

## Related Resources

- [Official Website](https://stitch.withgoogle.com/)
- [Stitch Documentation](https://scriptbyai.com/google-stitch/) — community-reviewed guide with pros/cons
- [Google AI Studio](https://aistudio.google.com/) — for further code generation from Stitch designs
- [Figma](https://www.figma.com/) — recommended refinement destination

## License

Stitch is an experimental Google Labs product; usage is governed by the terms shown on [stitch.withgoogle.com](https://stitch.withgoogle.com/).
