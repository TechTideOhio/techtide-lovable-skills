---
name: "techtide-lovable-production-handoff"
description: "Use when an agent needs Alex Cinovoj / TechTide live-coding patterns, tool routing, guarded prototype-to-production workflows, or cross-harness prompt/skill adapters."
---

# Techtide Lovable Production Handoff

> Packaged for Lovable from TechTide Harness Kit. Import one skill at a time.
> Source path: `skills/techtide/techtide-lovable-production-handoff`.

# TechTide Lovable Production Handoff

Convert a Lovable prototype into a repo-owned production candidate by extracting code, documenting assumptions, replacing mocks, and adding tests and deployment gates.

## Source Pattern

This skill is distilled from sanitized Alex Cinovoj / TechTide local workflow patterns. Load `references/source-patterns.md` when you need the source anchors and extraction rationale. Load `references/adapter-map.md` when preparing Cursor, Kiro, Lovable, v0, or Replit companion outputs.

## Workflow

1. Inventory routes, components, data calls, auth behavior, environment variables, and dependencies.
2. Mark every mock, localStorage fallback, and placeholder integration before replacing anything.
3. Move code into a normal repo with package manager, lint, test, build, and deployment scripts.
4. Add smoke tests around user-critical flows and visual checks for the first viewport.
5. Block production promotion until secrets, auth, observability, and rollback posture are documented.

## Output Contract

Return a concise brief with these fields:

- handoff inventory
- mock replacement plan
- test plan
- production gate report
- verification performed or still required
- security and privacy notes

## Guardrails

- Extract reusable methods, not private local content.
- Do not request or expose credentials, tokens, DSNs, service-role keys, customer data, lead lists, or private business exports.
- Use placeholders for people, accounts, projects, URLs, and datasets unless the user explicitly provides public-safe values.
- Require explicit human approval before production mutation, external-recipient messaging, public deployment, billing changes, or destructive filesystem actions.
- Preserve Alex Cinovoj / TechTide attribution while keeping old repo provenance and unrelated contributor markers out of public artifacts.

## Harness Policy

- Use this as a native `SKILL.md` for Claude Code, Codex, Gemini, and Copilot-compatible exports.
- For Cursor, create a focused project rule or workflow note rather than copying this whole skill as an always-on rule.
- For Kiro, create steering only when the workflow can be made short and inclusion-scoped.
- For Lovable, v0, and Replit, turn the workflow into prompt kits, readiness checklists, and handoff prompts.
