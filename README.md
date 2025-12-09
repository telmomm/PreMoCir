
# PreMoCir

Live demo: https://premocir.streamlit.app

Overview
--------
PreMoCir is a clinical prediction tool that estimates short-term mortality risk for patients undergoing cardiac procedures. The repository contains the Streamlit app, the trained model, helper scripts, and Jupyter notebooks used for data preparation and analysis.

Quick user guide
-----------------
Inputs expected by the app:

- Hematocrit (preoperative) — percentage value.
- Creatinine (preoperative) — mg/dL.
- Edmonton Frailty Score — integer 0–17.
- Hospital admission date — date field.
- MACE complications (toggle) — mark if major adverse cardiovascular events occurred.
- Any complications (toggle) — mark if any other relevant medical complication occurred.

How to run locally
-------------------
Requirements are listed in `requirements.txt`. A typical local run sequence is:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux (zsh)
pip install -r requirements.txt
streamlit run main.py
```

License
-------
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

