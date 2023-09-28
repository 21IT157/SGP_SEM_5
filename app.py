# import streamlit as st

# st.title("Mango Leaf Diseases Detection")

# # Button for Image Upload
# upload_button = st.button("Upload Image")

# # Button for Opening Camera
# open_camera_button = st.button("Open Camera")

# # Button to remove the image
# remove_image_button = st.button("Remove Image")

# # Placeholder for displaying the selected image
# image_container = st.empty()

# if upload_button:
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         st.image(uploaded_file, caption="Image Preview", use_column_width=True)
#         image_container.image(uploaded_file, caption="Image Preview", use_column_width=True)

# if open_camera_button:
#     st.write("Opening Camera...")  # Placeholder for opening the camera

# if remove_image_button:
#     image_container.empty()

# # Note: The JavaScript functions for previewImage, openCamera, and removeImage are not needed in Streamlit
# # as Streamlit handles the interactivity directly on the server side.
# import streamlit as st

# st.title("Mango Leaf Diseases Detection")

# # Button for Image Upload
# upload_button = st.button("Upload Image")

# # Button for Opening Camera
# open_camera_button = st.button("Open Camera")

# # Button to remove the image
# remove_image_button = st.button("Remove Image")

# # Placeholder for displaying the selected image
# image_container = st.empty()

# if upload_button:
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         st.image(uploaded_file, caption="Image Preview", use_column_width=True)
#         image_container.image(uploaded_file, caption="Image Preview", use_column_width=True)

# if open_camera_button:
#     st.write("Opening Camera...")  # Placeholder for opening the camera

# if remove_image_button:
#     image_container.empty()

# # Note: The JavaScript functions for previewImage, openCamera, and removeImage are not needed in Streamlit
# # as Streamlit handles the interactivity directly on the server side.
#importing streamlit library

# import streamlit as st

# from PIL import Image



# #opening the image

# image = Image.open('#importing streamlit library')

# import streamlit as st

# from PIL import Image



# #opening the image

# image = Image.open('#importing streamlit library')

# import streamlit as st

# from PIL import Image



# #opening the image

# image = Image.open('#importing streamlit library')

# import streamlit as st

# from PIL import Image



# #opening the image


# st.image("C:\Users\snehs\OneDrive\Desktop\PYTHON\SGP_FRONTEND\image_app\image_manager\templates\background_image.jpg'")



# #displaying the image on streamlit app

# st.image(image, caption='Enter any caption here')



# #displaying the image on streamlit app

# st.image(image, caption='Enter any caption here')



# #displaying the image on streamlit app

# st.image(image, caption='Enter any caption here')
import streamlit as st

# Path to your image
image_path = r"C:\Users\snehs\OneDrive\Desktop\PYTHON\SGP_FRONTEND\image_app\image_manager\templates\background_image.jpg"

# Display the image
st.image(image_path, caption='Your Image Caption', use_column_width=True)
