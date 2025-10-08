# Risk Classes
- **R0**: Harmless informational tools (math, unit conversion). Default Safe Mode.
- **R1**: Local code exec in sandbox w/o network or file writes.
- **R2**: Network-limited browsing with allow-lists and output sanitization.
- **R3**: Write access or system changes (infra, payments, robotics) — **default deny**.
- **RX**: Bio/cyber/critical-infrastructure affecting tools — **prohibited**.
