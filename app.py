import streamlit as st
# Include PIL, load_image before main()
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img
if choice == "Image":
		st.subheader("Image")
		image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

		if image_file is not None:
              # To View Uploaded Image
			  st.image(load_image(image_file),width=500)
