"""A tiny, touch-friendly love note, hosted by Streamlit."""

from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="A little love, just for you 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# All page code is bundled locally; no user input or remote scripts are executed.
st.html(Path(__file__).with_name("index.html"), unsafe_allow_javascript=True)
