#!/usr/bin/env python3
import sys, json, yaml, pathlib
from jsonschema import validate, Draft202012Validator

schema = json.load(open('schemas/capability_gates.schema.json'))
data = yaml.safe_load(open('GOVERNANCE/capability_gates.yaml'))

Draft202012Validator(schema).validate(data)
print('capability_gates.yaml ✓ schema valid')
