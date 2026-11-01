# For Divyani 💗

A small, phone-friendly love note for Divyani. Every tap shows **I love you 💗**, a burst of hearts, and one randomly selected message:

- Divyani, ek kissi day do na babu 😘💋
- thank u yrr for being my constant in my life
- love u babuuu
- Nenu ninnu pemistunnaanu 💖
- being my comfort zone as always

Each popup stays open with **Yes 💖** and **No 🙈** buttons. Hovering over or trying to select No makes the whole note dodge to another position inside the screen. Yes replies **muaahhh 😘💋💖**. Tapping elsewhere opens another random note. The buttons also work with a keyboard, and reduced-motion preferences are respected.

Live app: https://babu-love-note.streamlit.app/

## Run locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Host on Streamlit Community Cloud

1. Put `app.py`, `index.html`, `requirements.txt`, and `.streamlit/config.toml` in a GitHub repository, preserving the folder structure.
2. Sign in at https://share.streamlit.io/ and choose **Create app**, then deploy from GitHub.
3. Select the repository, branch `main`, and main file `app.py`.
4. Choose an available app address, then select **Deploy**.
5. Open the resulting `.streamlit.app` address and share it.

The page includes its own styling and illustration; no images, API keys, external scripts, or secrets are required. You can also open `index.html` directly in a browser for a standalone version.

To personalize the message, edit the visible text and the popup message in `index.html`.
