---
name: shadcn-ui
description: Expert in using shadcn/ui components for React/Astro projects.
---

# Shadcn/UI Guidelines

## Usage Strategy
When the user asks for a UI component (like a button, card, or slider):
1. **Do not write CSS from scratch.** Use the standard shadcn structure.
2. **Tailwind First:** Use standard Tailwind utility classes for layout.
3. **Radix UI:** Remember that shadcn is built on Radix UI primitives.

## Component Installation (Simulation)
Since we are in a static generation environment, if I need a component (e.g., a Button), I should:
1. Create the component file in `src/components/ui/button.tsx`.
2. Paste the standard shadcn code for that component (using `class-variance-authority` and `clsx`).
3. Ensure `tailwind.config.mjs` includes the correct paths.

## Style Guide for Olaizola Etxea
- **Radius:** 0.5rem (Rounded-lg)
- **Colors:** Map the user's palette to the CSS variables (`--primary`, `--secondary`) in `src/styles/globals.css`.