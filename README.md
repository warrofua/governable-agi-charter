# Governable-AGI Charter v1.1

**What’s new:** This version merges the original governance kit with a *proactive AGI pack* (risk classes, tripwires, audit/attestation, disclosure template, system prompt snippets, machine-readable addendum, evaluation matrix).

## Quick Start
- Adopt `GOVERNANCE/constraint_charter.md` (v1.1).
- Use `GOVERNANCE/tool_gating_policy.md` with **Risk Classes R0–R3, RX**.
- Validate files with `make validate` (schema checks).
- Open red-team findings via `.github/` issue forms.
- Publish incidents with `docs/public_disclosure_template.md`.

## Structure
- `GOVERNANCE/` — charter, tool gating policy, risk classes, tripwires, anti-collusion, oversight charter, incident templates
- `docs/` — model card, *machine-readable addendum*, safety dossier, provenance footer, public disclosure, system prompt snippets
- `schemas/` — JSON schemas for capability gates **and** model card addendum
- `scripts/` — validators, charter hash
- `.github/` — issue forms, PR template, CI workflow
- `tables/` — evaluation matrix CSV

_Repo generated 2025-10-07. Maintainer: ChatGPT (operating under the Constraint Charter v1.1)._
