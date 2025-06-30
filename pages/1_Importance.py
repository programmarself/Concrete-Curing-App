import streamlit as st
import os
from PIL import Image
import requests
from io import BytesIO

# --- Logo Display Function ---
def show_logo():
    """Display logo with error handling"""
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=150)
    else:
        st.sidebar.markdown("""
        <div style="text-align:center; padding:10px; border:1px solid #ccc; border-radius:5px;">
            <h3>🏗️ The Civil Tales</h3>
        </div>
        """, unsafe_allow_html=True)

# --- Image Display Function ---
def display_image(image_path, width=None, caption=None, fallback_text=None):
    """Safely display image with fallbacks"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, width=width, caption=caption)
            return True
        elif fallback_text:
            # Use placeholder if image missing
            placeholder_url = f"https://via.placeholder.com/{width or 600}x{width or 400}?text={fallback_text.replace(' ','+')}"
            img = Image.open(BytesIO(requests.get(placeholder_url).content))
            st.image(img, width=width, caption=caption or fallback_text)
            return True
    except Exception as e:
        st.warning(f"Image loading error: {str(e)}")
    
    if fallback_text:
        st.info(fallback_text)
    return False

# --- Display Logo ---
show_logo()

# --- Page Content ---
st.title("Why Curing is Important")

st.write("""
Proper concrete curing enhances strength, durability, and resistance to cracking. 
It ensures concrete achieves its intended design properties.
""")

tab1, tab2, tab3 = st.tabs(["Benefits", "Consequences", "Time Factors"])

with tab1:
    st.header("Benefits of Proper Curing")
    display_image(
        "assets/benefits.jpg", 
        width=400,
        fallback_text="Benefits of Proper Curing"
    )
    st.markdown("""
    - Maintains moisture for continued hydration
    - Increases strength gain over time
    - Reduces shrinkage cracks
    - Enhances surface hardness
    - Protects from thermal shrinkage
    """)

with tab2:
    st.header("Consequences of Poor Curing")
    display_image(
        "assets/cracks.jpg",
        width=400,
        fallback_text="Consequences of Poor Curing"
    )
    st.markdown("""
    - Cracks and dusting on surface
    - Poor durability and water penetration
    - Low compressive strength
    - Reduced structure lifespan
    """)

with tab3:
    st.header("Curing Time Factors")
    st.write("The standard curing time is 28 days, but depends on:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Cement type
        - Weather conditions
        - Mineral admixtures
        - Concrete mix design
        """)
    with col2:
        display_image(
            "assets/curing_time.jpg",
            width=300,
            fallback_text="Curing Time Factors"
        )
        # Footer with Font Awesome icons
st.markdown("---")
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
    .social-icons {
        margin: 20px 0;
    }
    .social-icons a {
        margin: 0 10px;
        color: #1E90FF;
        font-size: 24px;
        transition: color 0.3s, transform 0.3s;
        text-decoration: none;
    }
    .social-icons a:hover {
        color: #FF4500;
        transform: scale(1.2);
    }
    .footer {
        text-align: center;
        font-size: 16px;
        padding: 20px 0;
    }
    </style>
    <div class="footer">
      <p>&copy; 2025 Concrete Curing App | All rights reserved</p>
      <p><strong>Developed with ❤️ by Irfan Ullah Khan</strong></p>
      <div class="social-icons">
        <a href="https://github.com/programmarself" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/iukhan/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
        <a href="https://programmarself.github.io/My_Portfolio/" target="_blank" title="Portfolio"><i class="fas fa-briefcase"></i></a>
        <a href="mailto:programmarself@gmail.com" title="Email"><i class="fas fa-envelope"></i></a>
      </div>
    </div>
""", unsafe_allow_html=True)
