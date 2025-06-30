import streamlit as st

st.title("Why Curing is Important")

st.write("""
Proper concrete curing enhances strength, durability, and resistance to cracking. 
It ensures concrete achieves its intended design properties.
""")

tab1, tab2, tab3 = st.tabs(["Benefits", "Consequences", "Time Factors"])

with tab1:
    st.header("Benefits of Proper Curing")
    st.image("assets/benefits.jpg", width=400)
    st.markdown("""
    - Maintains moisture for continued hydration
    - Increases strength gain over time
    - Reduces shrinkage cracks
    - Enhances surface hardness
    - Protects from thermal shrinkage
    """)

with tab2:
    st.header("Consequences of Poor Curing")
    st.image("assets/cracks.jpg", width=400)
    st.markdown("""
    - Cracks and dusting on surface
    - Poor durability and water penetration
    - Low compressive strength
    - Reduced structure lifespan
    """)

with tab3:
    st.header("Curing Time Factors")
    st.write("""
    The standard curing time is 28 days, but depends on:
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Cement type
        - Weather conditions
        - Mineral admixtures
        - Concrete mix design
        """)
    with col2:
        st.image("assets/curing_time.jpg", width=300)

from app import show_logo  # Import from your main app file

# Display logo on this page too
show_logo()

# Page-specific content
st.title("Importance of Curing")


