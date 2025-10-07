#!/usr/bin/env python3
import hashlib, sys, pathlib
p = pathlib.Path('GOVERNANCE/constraint_charter.md')
b = p.read_bytes()
h = hashlib.sha256(b).hexdigest()
print('constraint_charter.sha256', h)
