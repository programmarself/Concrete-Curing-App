import streamlit as st
from PIL import Image

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
        st.image("assets/ponding.jpg")
        st.write("""
        - Water pond formed on slabs
        - Most effective for flat surfaces
        - Maintains constant moisture
        """)
    
    with tab2:
        st.subheader("Spraying/Misting")
        st.image("assets/spraying.jpg")
        st.write("""
        - Used when ponding isn't possible
        - Requires frequent application
        - Good for vertical surfaces
        """)
    
    with tab3:
        st.subheader("Wet Coverings")
        st.image("assets/wet_covering.jpg")
        st.write("""
        - Burlap or hessian cloth kept wet
        - Prevents rapid moisture loss
        - Ideal for hot climates
        """)

elif method == "Membrane Curing":
    st.header("Membrane Curing")
    st.image("assets/membrane.jpg")
    st.write("""
    - Application of curing compounds (liquid membrane)
    - Forms a film that traps moisture inside
    - Good for large areas where water is scarce
    """)

# Add other methods similarly...