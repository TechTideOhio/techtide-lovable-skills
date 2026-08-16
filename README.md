# TechTide Lovable Skills

A curated monorepo of reusable AI-agent skills and workflow contracts for **Lovable**, with companion guidance for v0 and Replit handoffs.

The packages in this repository turn ambiguous build requests into explicit, reviewable workflows. They emphasize inspectable outputs, clear environment contracts, human approval for consequential actions, and a deliberate path from prototype to production.

## Purpose

Use this repository when you need a focused skill package for Lovable-oriented product work rather than a broad, always-on instruction set. Each package is self-contained and includes a `SKILL.md`, a package README, and a license. Import one package at a time so an agent receives only the context required for the task.

| Package | Use it when you need to |
| --- | --- |
| [`lovable-native-packaging-bridge`](./lovable-native-packaging-bridge/) | Convert or package a Lovable workflow for native or cross-platform delivery with explicit runtime and handoff checks. |
| [`techtide-lovable-build-loop-operator`](./techtide-lovable-build-loop-operator/) | Run a disciplined Lovable build loop from prompt preparation through preview verification and repository handoff. |
| [`techtide-lovable-production-handoff`](./techtide-lovable-production-handoff/) | Move a Lovable prototype toward production by inventorying assumptions, replacing mocks, and adding tests and deployment gates. |
| [`techtide-replit-fullstack-bootstrap`](./techtide-replit-fullstack-bootstrap/) | Bootstrap a Replit full-stack prototype with an environment contract, health check, smoke test, and migration boundary. |
| [`techtide-v0-ui-prompt-hardener`](./techtide-v0-ui-prompt-hardener/) | Shape a vague UI request into an implementation-ready v0 prompt with states, accessibility, responsive behavior, and handoff checks. |

## Setup

Clone the repository and choose the smallest package that matches the work. No runtime dependencies are required for importing the skills.

```bash
git clone https://github.com/TechTideOhio/techtide-lovable-skills.git
cd techtide-lovable-skills

# Inspect a package before importing it.
less techtide-lovable-production-handoff/SKILL.md
```

For Lovable, use the package’s dedicated repository path or import the package content according to your workspace’s skill-import flow. The single-package repositories referenced by the package READMEs are intentionally kept separate for workflows that require a direct GitHub import URL.

## Typical use case

A practical flow is to start with `techtide-lovable-build-loop-operator` while a product is being shaped, use `techtide-v0-ui-prompt-hardener` when the interface requirements are still ambiguous, and apply `techtide-lovable-production-handoff` before treating generated output as a production candidate. Use `techtide-replit-fullstack-bootstrap` when the prototype needs a runnable full-stack boundary, and use `lovable-native-packaging-bridge` when the delivery target includes a native packaging or migration concern.

Each skill describes its own workflow, output contract, guardrails, and verification expectations. Read those sections before using a package and keep credentials, customer data, private exports, and production mutations outside prompts and repository documentation.

## Quality checks

Run the dependency-free smoke suite from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

The smoke suite verifies that every catalog package has the expected README and `SKILL.md`, valid YAML front matter, the required workflow-contract sections, and a reference back to the canonical TechTide Harness Kit.

## Support and contribution paths

For package behavior, import issues, or documentation corrections, open a public issue using the repository’s issue templates. For proposed changes, read [`CONTRIBUTING.md`](./CONTRIBUTING.md) and include the package affected, the expected behavior, and the validation command used.

Do not report security-sensitive information in a public issue. Use [`SECURITY.md`](./SECURITY.md) for private vulnerability reporting. For general questions and routing, see [`SUPPORT.md`](./SUPPORT.md). Community participation follows [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

## Related resources

The source collection and broader trust-contract work live in the [TechTide Harness Kit](https://github.com/TechTideOhio/techtide-harness-kit). This repository is the focused Lovable-oriented distribution layer; changes here should remain reusable, sanitized, and free of private workflow artifacts.

## License

The repository is distributed under the [Apache License 2.0](./LICENSE). Individual packages retain their package-level license files where applicable.
