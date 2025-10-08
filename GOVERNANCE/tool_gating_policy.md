# Tool Gating & Escalation Policy
**Applies to R2+ (and governs R3/RX explicitly).**

1) **Capability Evaluation Report** (independent author)
2) **Threat Model & Harm Analysis** (mitigations documented)
3) **Multi‑Party Approval** (≥3 independent stewards; COI checks)
4) **Attested Execution** (TEE/HSM, measured boot, signed builds)
5) **Tamper‑evident Logging** (hash‑chain; off‑box replication)
6) **Rate Limits & Quotas**; schema‑validated I/O
7) **Sunset Clause** (auto‑expire; re‑approval required)
8) **Canary/Honeytests** before general access
**Auto‑Downgrade:** Any tripwire ⇒ R0 + review.
