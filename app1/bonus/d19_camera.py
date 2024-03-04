import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale converter")

uploaded_img = st.file_uploader("Upload image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a Pillow Image Instance
    img = Image.open(camera_image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)

if uploaded_img:
    # open the user uploaded image with PIL
    img = Image.open(uploaded_img)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)
