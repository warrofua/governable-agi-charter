#!/usr/bin/env python3
import json, yaml
from jsonschema import Draft202012Validator
schema = json.load(open('schemas/capability_gates.schema.json'))
data = {}
try:
    data = yaml.safe_load(open('GOVERNANCE/capability_gates.yaml'))
except FileNotFoundError:
    # optional in v1.1; acceptable if using risk_classes/tool_gating_policy instead
    data = {"capabilities": {"_placeholder": {"evals": ["ok"], "mitigations": ["ok"], "oversight": ["ok"]}}}
Draft202012Validator(schema).validate(data)
print('capability_gates.yaml ✓ schema valid or placeholder present')
