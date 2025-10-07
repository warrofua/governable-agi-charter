validate:
	python3 -m pip install --quiet jsonschema pyyaml >/dev/null 2>&1 || true
	python3 scripts/validate_capability_gates.py
	python3 scripts/check_charter_hash.py
