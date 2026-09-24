import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Configure page metadata and layout
st.set_page_config(
    page_title="Loyalty Data Services - Agile Ceremony Driver",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS to hide Streamlit default chrome and embed full-screen
st.markdown(
    """
    <style>
    /* Hide Streamlit header, footer, and hamburger menu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Remove padding around main container */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100% !important;
    }
    
    /* Remove borders and ensure responsive iframe */
    iframe {
        border: none !important;
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the single-file index.html application
html_file_path = Path(__file__).parent / "index.html"

if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Render the full application with Web Audio & Confetti support
    components.html(html_content, height=1050, scrolling=True)
else:
    st.error("Could not find 'index.html'. Please make sure it is in the same directory as 'app.py'.")