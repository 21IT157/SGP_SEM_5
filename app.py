import streamlit as st

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

# # Include PIL, load_image before main()
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

...

if choice == "Image":
		st.subheader("Image")
		image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

		if image_file is not None:

			  # To See details
			  file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
			  st.write(file_details)

              # To View Uploaded Image
			  st.image(load_image(image_file),width=250)
