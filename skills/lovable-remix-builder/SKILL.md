---
name: lovable-remix-builder
description: Builds high-converting landing pages and marketing sites in Lovable by remixing reference sites section by section. Use when the user wants a premium website style rebuilt for a new brand, niche, or client without designing from scratch.
---

# Lovable Remix Builder

Use this skill when the user wants:
- a beautiful website built fast in Lovable
- a premium SaaS or marketing-site style based on references
- a section-by-section remix workflow instead of one giant vague prompt
- a site restyled for a new company, church, client, or product
- a homepage style extended into secondary pages like `About`, `Pricing`, or `Contact`
- a landing page rebuilt from a scraped JSON export that already contains branding and markdown

## Core Principle

Do not start by asking Lovable to invent everything from nothing.

Start with:
1. strong references
2. a clear section plan
3. consistent visual language
4. one section at a time

The goal is not to clone a site exactly. The goal is to borrow structure, pacing, and conversion patterns, then rebuild them for the user's content.

## Reference Selection Rules

When evaluating references, prefer sites that clearly show:
- one strong headline
- one primary call to action
- one clear demo image, hero visual, or product proof

Avoid references that are:
- visually impressive but unclear
- overloaded with decorative motion
- weak on CTA clarity
- impossible to translate to mobile cleanly

See [references/reference-selection.md](references/reference-selection.md).

## Default Workflow

### 1. Pick the references
- Ask for 1-3 reference sites or choose them from the user's description.
- Break each reference into sections:
  - navbar
  - hero
  - feature grid
  - social proof / logo row
  - demo section
  - CTA
  - footer

If the user gives you a scraped JSON export instead of screenshots, parse it first:
- branding colors
- typography
- primary and secondary CTAs
- markdown section order
- logo and media URLs

See [references/json-scrape-remix.md](references/json-scrape-remix.md).

### 2. Extract the useful structure
- Use screenshots, notes, or Figma / Relume style section breakdowns if available.
- Preserve only the high-value layout decisions.
- Keep typography, color, and spacing coherent across sections.

### 3. Write section prompts for Lovable
- Prompt the hero first.
- Then add sections one at a time.
- For every new section, explicitly say:
  - follow the existing styles
  - keep the same colors, type scale, and spacing language
  - keep mobile responsiveness clean

See [references/lovable-prompt-patterns.md](references/lovable-prompt-patterns.md).

### 4. Add media
- Replace static hero images with hosted videos when useful.
- If the user wants a background video, give Lovable the exact behavior:
  - autoplay
  - muted
  - loop
  - no controls
  - edge-to-edge coverage

### 5. Rewrite for the target brand
- Once the layout is working, rewrite all content for the user's actual niche or company.
- Preserve the conversion structure while replacing:
  - headline
  - subhead
  - features
  - CTA copy
  - page naming

### 6. Extend the system
- Ask Lovable to create secondary pages following the homepage style.
- Keep page-level consistency explicit.

### 7. Validate
- Check desktop and mobile after every major addition.
- If one section breaks mobile, fix that section before stacking on more.

## Prompting Rules

- Keep prompts direct and concrete.
- Prefer “add one section below with these constraints” over giant all-in-one prompts.
- When restyling, explicitly tell Lovable to preserve existing style tokens.
- When rewriting content, tell it to keep structure but change the brand, audience, and use case.

## Deliverables

By default, produce:
1. the section plan
2. the Lovable prompts in order
3. any content rewrite prompts
4. any secondary-page prompts
5. a short mobile QA checklist

## Common Requests

- “Use this SaaS site as reference and rebuild it for my company.”
- “Make a homepage in Lovable using the same dark premium feel as this example.”
- “Rewrite this whole site for a church in Vietnam.”
- “Create an About Us page following the homepage styles.”
