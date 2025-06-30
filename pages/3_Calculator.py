import streamlit as st
import numpy as np
import pandas as pd
import os


st.title("Concrete Curing Calculator")

st.write("""
Estimate the required curing time based on your project conditions.
""")

cement_type = st.selectbox(
    "Cement Type",
    ["Ordinary Portland Cement", "Portland Pozzolana Cement", "Rapid Hardening Cement"]
)

weather = st.select_slider(
    "Weather Conditions",
    options=["Very Cold", "Cold", "Moderate", "Warm", "Hot"]
)

admixtures = st.checkbox("Using mineral admixtures")

# Calculation logic
base_days = 7
if cement_type == "Portland Pozzolana Cement":
    base_days += 3
elif cement_type == "Rapid Hardening Cement":
    base_days -= 2

weather_factors = {
    "Very Cold": 5,
    "Cold": 3,
    "Moderate": 0,
    "Warm": 2,
    "Hot": 4
}

total_days = base_days + weather_factors[weather]
if admixtures:
    total_days += 2

st.subheader("Recommended Curing Duration")
st.metric("Minimum Wet Curing Days", total_days)

st.info("""
Note: This is a general guideline. Always follow project specifications 
and consult with structural engineers for critical applications.
""")

# Sidebar with just the logo/title
st.sidebar.title("The Civil Tales")
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
else:
    st.sidebar.markdown("""
    <div style="text-align:center; padding:10px; border:1px solid #ccc; border-radius:5px;">
        <h3>The Civil Tales</h3>
    </div>
    """, unsafe_allow_html=True)
