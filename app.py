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

# Footer with Font Awesome icons
st.markdown("---")
st.markdown("""
    <style>
    .social-icons a {
        margin: 0 10px;
        color: #1E90FF;
        font-size: 24px;
        transition: color 0.3s, transform 0.3s;
    }
    .social-icons a:hover {
        color: #FF4500;
        transform: scale(1.2);
    }
    </style>
    <div style='text-align: center; font-size: 16px;'>
      <p>&copy; 2025 Concrete Curing App | All rights reserved</p>
      <p><strong>Developed with ❤️ by Irfan Ullah Khan</strong></p>
      <div class='social-icons'>
        <a href="https://github.com/programmarself" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/iukhan/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
        <a href="https://programmarself.github.io/My_Portfolio/" target="_blank" title="Portfolio"><i class="fa fa-briefcase"></i></a>
        <a href="mailto:programmarself@gmail.com" title="Email"><i class="fas fa-envelope"></i></a>
      </div>
    </div>
""", unsafe_allow_html=True)
