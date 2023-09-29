import streamlit as st
from PIL import Image

st.title("Image Uploader and Preview")

# Function to upload and display the image
def load_image():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        return uploaded_file

# Load and display the image
image_file = load_image()

if image_file:
    st.write("You selected the following image:")
    st.image(image_file, use_column_width=True)
