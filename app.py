import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="KIPM-UP Absensi",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hilangkan padding default Streamlit agar HTML full-screen
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    .stApp {
        margin: 0;
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)

# Baca file index.html
html_file = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Tampilkan HTML full-screen dengan tinggi 100vh
    components.html(
        html_content,
        height=900,
        scrolling=True
    )
else:
    st.error("❌ File index.html tidak ditemukan! Pastikan index.html ada di folder yang sama dengan app.py")
