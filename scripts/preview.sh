#!/usr/bin/env bash
set -euo pipefail
python3 -m venv .venv || true
source .venv/bin/activate
pip install -q mkdocs-material
mkdocs serve -a 127.0.0.1:8000
