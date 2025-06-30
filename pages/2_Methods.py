import streamlit as st
from PIL import Image
import os
import requests
from io import BytesIO

def display_image(image_path, width=None, caption=None, fallback_text=None):
    """
    Safely display an image with multiple fallback options
    """
    # Try local file first
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            st.image(image, width=width, caption=caption)
            return True
        except Exception as e:
            st.warning(f"Error loading local image: {str(e)}")
    
    # Try online placeholder as fallback
    try:
        if fallback_text:
            placeholder_url = "https://via.placeholder.com/600x400.png?text=" + fallback_text.replace(" ", "+")
            response = requests.get(placeholder_url)
            online_image = Image.open(BytesIO(response.content))
            st.image(online_image, width=width, caption=caption or f"Placeholder: {fallback_text}")
            return True
    except Exception as e:
        st.error(f"Couldn't load image: {str(e)}")
    
    # Final fallback to text
    if fallback_text:
        st.info(fallback_text)
    return False

# Main app content
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
    
    with tab2:
        st.subheader("Spraying/Misting")
        display_image(
            "assets/spraying.jpg",
            width=400,
            fallback_text="Spraying: Worker applying water mist to concrete"
        )
        st.write("""
        - Used when ponding isn't practical
        - Requires frequent application (every 2-3 hours)
        - Good for vertical surfaces and complex shapes
        - Prevents surface drying between applications
        - Uses fine mist to avoid surface damage
        """)
    
    with tab3:
        st.subheader("Wet Coverings")
        display_image(
            "assets/wet_covering.jpg",
            width=400,
            fallback_text="Wet Coverings: Burlap covering on curing concrete"
        )
        st.write("""
        - Burlap or hessian cloth kept continuously wet
        - Prevents rapid moisture loss
        - Ideal for hot and windy climates
        - Coverings must remain wet at all times
        - Can be combined with plastic sheeting
        """)

elif method == "Membrane Curing":
    st.header("Membrane Curing")
    display_image(
        "assets/membrane.jpg",
        width=400,
        fallback_text="Membrane: Worker applying curing compound"
    )
    st.write("""
    - Application of curing compounds (liquid membrane)
    - Forms a film that traps moisture inside
    - Good for large areas where water is scarce
    - Typically sprayed or rolled on surface
    - White compounds help reflect sunlight
    - Must be applied after bleeding water evaporates
    """)
    st.warning("Note: Membrane curing requires proper surface preparation for effective bonding")

elif method == "Steam Curing":
    st.header("Steam Curing")
    display_image(
        "assets/steam_curing.jpg",
        width=400,
        fallback_text="Steam Curing: Precast elements in curing chamber"
    )
    st.write("""
    - Used in precast concrete industries
    - Accelerates strength gain using heat and moisture
    - Suitable for cold climates or fast-track projects
    - Typical temperature range: 50-75°C (122-167°F)
    - Requires controlled environment (curing chambers)
    - Often used with high-early-strength cement
    """)
    st.info("Steam curing cycles typically include: Initial delay → Temperature rise → Constant temperature → Cooling down")

elif method == "Plastic Sheeting":
    st.header("Plastic Sheeting")
    display_image(
        "assets/plastic_sheeting.jpg",
        width=400,
        fallback_text="Plastic Sheeting: Concrete covered with polyethylene"
    )
    st.write("""
    - Concrete covered with plastic sheets (usually polyethylene)
    - Reduces moisture loss effectively
    - Prevents evaporation without water application
    - Effective when water or curing compound isn't available
    - Sheets must be sealed at edges and overlaps
    - White plastic reflects sunlight, black absorbs heat
    """)
    st.warning("Ensure sheets are in full contact with concrete surface to prevent discoloration")

elif method == "Formwork Curing":
    st.header("Curing by Leaving Formwork")
    display_image(
        "assets/formwork_curing.jpg",
        width=400,
        fallback_text="Formwork Curing: Concrete column with formwork still in place"
    )
    st.write("""
    - Especially for vertical members like columns, walls
    - Formwork acts as a barrier to moisture loss
    - Useful during early curing stages (first 2-3 days)
    - Wood formwork provides better moisture retention
    - Metal formwork may require additional measures
    - Often combined with other methods after form removal
    """)
    st.info("Formwork curing is most effective in moderate climate conditions")

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
