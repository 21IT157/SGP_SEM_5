import streamlit as st

st.title("Mango Leaf Diseases Detection")

# Button for Image Upload
upload_button = st.button("Upload Image")

# Button for Opening Camera
open_camera_button = st.button("Open Camera")

# Button to remove the image
remove_image_button = st.button("Remove Image")

# Placeholder for displaying the selected image
image_container = st.empty()

if upload_button:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Image Preview", use_column_width=True)
        image_container.image(uploaded_file, caption="Image Preview", use_column_width=True)
image = Image.open(uploaded_file)



#displaying the image on streamlit app

st.image(image, caption='Enter any caption here')
if open_camera_button:
    st.write("Opening Camera...")  # Placeholder for opening the camera

if remove_image_button:
    image_container.empty()

# Note: The JavaScript functions for previewImage, openCamera, and removeImage are not needed in Streamlit
# as Streamlit handles the interactivity directly on the server side.
