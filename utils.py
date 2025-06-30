# utils.py
import streamlit as st
import os

def show_logo():
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=150)
    else:
        st.sidebar.markdown("""
        <div style="text-align:center;">
            <h3>🏗️ The Civil Tales</h3>
        </div>
        """, unsafe_allow_html=True)
