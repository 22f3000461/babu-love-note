# For Divyani 💗

A small, phone-friendly love note for Divyani. Tap anywhere for **I love you 💗**, **Divyani, ek kissi day do na babu 😘💋**, and a burst of hearts. The main button also works with a keyboard. Reduced-motion preferences are respected.

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
