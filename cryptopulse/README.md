# CryptoPulse Streamlit App

This folder contains the Streamlit integration for the CryptoPulse frontend.

## Install dependencies

```bash
cd "CryptoPulse/cryptopulse"
python3 -m pip install -r requirements.txt
```

## Run the Streamlit app

```bash
cd "CryptoPulse/cryptopulse"
streamlit run streamlit_app.py --server.port 8501
```

Then open:

```text
http://localhost:8501
```

## Static website

The existing static website is still available via `index.html`, `dashboard.html`, `portfolio.html`, and `analytics.html`.

The static pages also include a navigation link to the Streamlit app.
