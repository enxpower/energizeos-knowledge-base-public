$ErrorActionPreference = "Stop"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install mkdocs-material
mkdocs serve -a 127.0.0.1:8000
