# Contributing

Thank you for improving the TechTide Lovable Skills catalog. Contributions should make a package more reusable, explicit, and safe for public distribution.

## Before opening a change

Read the affected package’s `SKILL.md` and README. Confirm that the proposed change belongs in this repository rather than in a private workflow, customer-specific prompt, or project-owned application repository. Do not include credentials, private URLs, customer data, internal exports, or unverified claims.

## Change expectations

Keep each pull request focused on one package or one repository-wide concern. Preserve the package contract: clear workflow steps, an output contract, guardrails, and verification guidance. Update the package README when its import path or intended use changes. Prefer plain Markdown and the Python standard library for repository checks unless a dependency is necessary and documented.

## Validation

Run the smoke suite before opening a pull request:

```bash
python3 -m unittest discover -s tests -v
```

Describe the package affected, the user problem addressed, the documentation or behavior change, and the validation performed. Maintainers may request additional examples or a narrower scope when a change increases prompt coupling or introduces unsupported platform assumptions.

## Pull requests

Use the pull-request template. Changes to safety guardrails, import instructions, or source attribution require especially careful review because they affect downstream agent behavior.
