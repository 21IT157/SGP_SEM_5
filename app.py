import streamlit as st

# Function to render page content
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")

def page_leaf(image_file):
    st.title("Leaf Diagonisis")
    st.write("Upload your image here to check the health of the leaf")
          img = Image.open(image_file)
	return img
          if choice == "Image":
                    st.subheader("Image")
                    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
                    st.image(load_image(image_file),width=250)


pages = {
    "Home": page_home,
    "About": page_leaf,
}
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
if selected_page in pages:
    pages[selected_page]()
