import streamlit as st
from PIL import Image
import os

# App configuration
st.set_page_config(
    page_title="Concrete Curing Guide",
    page_icon="🏗️",
    layout="wide"
)

# Function to load images safely
def load_image(image_path, width=None):
    try:
        image = Image.open(image_path)
        if width:
            return st.image(image, width=width)
        return st.image(image)
    except FileNotFoundError:
        st.warning(f"Image not found at path: {image_path}")
        return None
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

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

# Main content - all on one page with sections
st.title("Concrete Curing Methods Guide")
st.subheader("Every good structure begins with proper curing!")

# Home Section
st.markdown("---")
st.header("Introduction to Concrete Curing")
col1, col2 = st.columns(2)

with col1:
    home_image_path = os.path.join("assets", "home_image.jpg")
    if os.path.exists(home_image_path):
        st.image(home_image_path, caption="Proper curing ensures durable concrete")
    else:
        st.info("Default curing process illustration")
    
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

# Importance of Curing Section
st.markdown("---")
st.header("Why Curing is Important")

tab1, tab2, tab3 = st.tabs(["Benefits", "Consequences", "Time Factors"])

with tab1:
    st.subheader("Benefits of Proper Curing")
    st.markdown("""
    - Maintains moisture for continued hydration
    - Increases strength gain over time
    - Reduces shrinkage cracks
    - Enhances surface hardness
    - Protects from thermal shrinkage
    """)

with tab2:
    st.subheader("Consequences of Poor Curing")
    st.markdown("""
    - Cracks and dusting on surface
    - Poor durability and water penetration
    - Low compressive strength
    - Reduced structure lifespan
    """)

with tab3:
    st.subheader("Curing Time Factors")
    st.write("""
    The standard curing time is 28 days, but depends on:
    """)
    st.markdown("""
    - Cement type
    - Weather conditions
    - Mineral admixtures
    - Concrete mix design
    """)

# Curing Methods Section
st.markdown("---")
st.header("Concrete Curing Methods")

method = st.selectbox(
    "Select a curing method to learn more:",
    ["Water Curing", "Membrane Curing", "Steam Curing", "Plastic Sheeting", "Formwork Curing"]
)

if method == "Water Curing":
    st.subheader("Water Curing (Most Effective)")
    st.markdown("""
    - **Ponding**: Water pond formed on slabs
    - **Spraying/Misting**: Used when ponding isn't possible
    - **Wet Coverings**: Burlap or hessian cloth kept wet
    """)
    st.write("*Simple & ideal for hot climates*")

elif method == "Membrane Curing":
    st.subheader("Membrane Curing")
    st.markdown("""
    - Application of curing compounds (liquid membrane)
    - Forms a film that traps moisture inside
    - Good for large areas where water is scarce
    """)

elif method == "Steam Curing":
    st.subheader("Steam Curing")
    st.markdown("""
    - Used in precast industries
    - Accelerates strength gain using heat and moisture
    - Suitable for cold climates or fast-track projects
    """)

elif method == "Plastic Sheeting":
    st.subheader("Plastic Sheeting")
    st.markdown("""
    - Concrete is covered with plastic sheets
    - Reduces moisture loss effectively
    - Prevents evaporation
    """)

elif method == "Formwork Curing":
    st.subheader("Curing by Leaving Formwork")
    st.markdown("""
    - Especially for vertical members like columns
    - Formwork acts as a barrier to moisture loss
    - Useful during early curing stages
    """)

# Curing Calculator Section
st.markdown("---")
st.header("Concrete Curing Calculator")

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
