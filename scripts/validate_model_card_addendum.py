#!/usr/bin/env python3
import json
from jsonschema import Draft202012Validator
schema = json.load(open('schemas/model_card_addendum.schema.json'))
data = json.load(open('docs/model_card_addendum.json'))
Draft202012Validator(schema).validate(data)
print('model_card_addendum.json ✓ schema valid')
