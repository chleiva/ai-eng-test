# Senior AI Assignment Pack

Starter pack for a short Senior AI Engineer take-home exercise.

Included:
- `ASSIGNMENT.md`
- `data/catalog.jsonl`
- `data/sample_questions.json`
- minimal Python starter app in `app/`

Notes:
- the dataset is synthetic and intended for assessment use
- the starter is intentionally incomplete and non-prescriptive

## Quick Start
Create a virtual environment, install the package, and run the starter:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
catalog-assistant
```

You can also run it non-interactively:

```bash
catalog-assistant --tenant harvestmart --question "Show me vegan breakfast products under 10 pounds"
```

## Important Files
- `ASSIGNMENT.md`
- `data/README.md`
- `data/catalog.jsonl`
- `data/sample_questions.json`
- `app/main.py`
- `app/retrieval.py`
- `app/prompting.py`
