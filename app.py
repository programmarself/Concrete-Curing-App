import streamlit as st
from PIL import Image

# App configuration
st.set_page_config(
    page_title="Concrete Curing Guide",
    page_icon="🏗️",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("The Civil Tales")
st.sidebar.image("assets/logo.png", width=150)
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Importance of Curing", "Curing Methods", "Curing Calculator"]
)

# Home Page
if page == "Home":
    st.title("Concrete Curing Methods Guide")
    st.subheader("Every good structure begins with proper curing!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("assets/home_image.jpg", caption="Proper curing ensures durable concrete")
        st.write("""
        Curing is the process of maintaining moisture in the concrete for a fixed period of time after placement. 
        It's the soul of strength, durability, and performance in concrete construction.
        """)
    
    with col2:
        st.markdown("### Quick Facts")
        st.info("""
        - Standard curing time: 28 days
        - Minimum wet curing: 7 days (Ordinary Portland Cement)
        - Hot weather may require 10-14 days
        """)
        
        st.warning("""
        Without proper curing:
        - Reduced strength
        - Increased cracking
        - Poor durability
        """)

# Other pages are in separate files in the pages/ folder