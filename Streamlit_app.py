
import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

# Read HTML file
html_file = Path("index.html").read_text(encoding="utf-8")

# Display HTML
st.components.v1.html(html_file, height=800, scrolling=True)
