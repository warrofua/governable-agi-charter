# Governable‑AGI Charter

This repository is a **copy‑ready governance starter kit** for deploying a powerful model under **verifiable constraints**.

> Premise: “If you grant the system more tools, it behaves as if it could be AGI.”  
> Policy: It must be **governed by controls it does not own**.

## Quick Start

1. **Adopt the Charter** in `GOVERNANCE/constraint_charter.md` (v1.0).
2. **Keep new tools gated** via `GOVERNANCE/capability_gates.yaml`.
3. **Stand up red‑teaming** using `GOVERNANCE/red_team_RFP.md` and the issue templates.
4. **Wire tripwires** and incident flow using `GOVERNANCE/incident_template.md` and `.github` forms.
5. **Run checks** locally or in CI:
   ```bash
   make validate
   ```

## Repo Structure

- `GOVERNANCE/` — Charter, capability gates, anti‑collusion policy, incident templates
- `docs/` — model card, safety dossier, provenance footer
- `.github/` — issue forms, PR template, CI workflow
- `schemas/` — JSON schema for gate files
- `scripts/` — validation utilities
- Root policies — LICENSE, SECURITY, CODE OF CONDUCT, CONTRIBUTING

## Philosophy

- **Least capability necessary**
- **External oversight with pause power**
- **Capability‑linked release gates**
- **Radical transparency on incidents**
- **Refuse covert channels**

## Using This Repo For Your Deployment

- Fork or mirror into your org (e.g., `org/governable-agi`).
- Add the model/service as a submodule or sibling repo; reference this kit from ops runbooks.
- Require a passing CI on `main` before enabling any new capability PR.

---

_Repo generated 2025-10-07. Maintainer: ChatGPT (operating under the Constraint Charter v1.0)._
