import streamlit as st
from PIL import Image
import os
import requests
from io import BytesIO

# --- Self-contained utility functions ---
def show_logo():
    """Display logo in sidebar with error handling"""
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=150)
    else:
        st.sidebar.markdown("""
        <div style="text-align:center; padding:10px; border:1px solid #ccc; border-radius:5px;">
            <h3>🏗️ The Civil Tales</h3>
        </div>
        """, unsafe_allow_html=True)

def display_image(image_path, width=None, caption=None, fallback_text=None):
    """Safely display image with fallbacks"""
    # Try local file first
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            st.image(img, width=width, caption=caption)
            return True
        except Exception as e:
            st.warning(f"Error loading local image: {str(e)}")
    
    # Try online placeholder if specified
    if fallback_text:
        try:
            placeholder_url = f"https://via.placeholder.com/{width or 600}x{width or 400}?text={fallback_text.replace(' ','+')}"
            img = Image.open(BytesIO(requests.get(placeholder_url).content))
            st.image(img, width=width, caption=caption or fallback_text)
            return True
        except Exception as e:
            st.error(f"Couldn't load placeholder: {str(e)}")
    
    # Final fallback to text
    if fallback_text:
        st.info(fallback_text)
    return False

# --- Display Logo ---
show_logo()

# --- Main Content (your original code remains unchanged below) ---
st.title("Concrete Curing Methods")

method = st.selectbox(
    "Select a curing method to learn more:",
    ["Water Curing", "Membrane Curing", "Steam Curing", "Plastic Sheeting", "Formwork Curing"]
)

if method == "Water Curing":
    st.header("Water Curing (Most Effective)")
    tab1, tab2, tab3 = st.tabs(["Ponding", "Spraying/Misting", "Wet Coverings"])
    
    with tab1:
        st.subheader("Ponding")
        display_image(
            "assets/ponding.jpg",
            width=400,
            fallback_text="Ponding: Water pond formed on concrete slab"
        )
        st.write("""
        - Water pond formed on slabs
        - Most effective for flat surfaces
        - Maintains constant moisture
        - Ideal for large horizontal surfaces
        - Requires proper containment of water
        """)
    
    # [Rest of your original content remains exactly the same...]
    # Include all other curing method sections exactly as you had them

# Final section with comparison
st.markdown("---")
st.subheader("Method Comparison")
comparison_data = {
    "Method": ["Water Curing", "Membrane Curing", "Steam Curing", "Plastic Sheeting", "Formwork Curing"],
    "Best For": ["Quality projects in all climates", "Large areas, water scarcity", "Precast, cold climates", "When water isn't available", "Vertical members"],
    "Labor Intensity": ["High", "Medium", "High", "Low", "Low"],
    "Cost": ["Low", "Medium", "High", "Low", "Low-Medium"],
    "Effectiveness": ["★★★★★", "★★★★", "★★★★", "★★★", "★★★"]
}
st.table(comparison_data)

st.caption("Note: All methods require proper execution to be effective. Choose based on project requirements and conditions.")
