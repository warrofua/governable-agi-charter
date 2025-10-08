#!/usr/bin/env python3
import hashlib, pathlib
p = pathlib.Path('GOVERNANCE/constraint_charter.md')
print('constraint_charter.sha256', hashlib.sha256(p.read_bytes()).hexdigest())
