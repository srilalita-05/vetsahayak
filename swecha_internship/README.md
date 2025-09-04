# 🐾 Vetsahayak — Streamlit MVP

A minimal, safe-by-default veterinary helper chatbot built with Streamlit.

## Features
- English & Telugu answers for core FAQs
- Emergency keyword triage with clear 'see a vet' guidance
- No medication dosing
- Simple FAQ retrieval (fuzzy + keywords)
- Clean Streamlit UI with quick action buttons

## Run locally
```bash
# 1) Create & activate venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run
streamlit run app.py
```

## Project layout
```
vetsahayak_mvp/
├─ app.py
├─ utils.py
├─ requirements.txt
├─ data/
│  ├─ faqs.csv
│  └─ emergency.json
└─ README.md
```

## Extend later
- Add more FAQs into `data/faqs.csv`
- Hook an LLM (OpenAI/HF) when you're ready; keep safety rules
- Add appointment links & vet directory for your region
