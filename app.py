import streamlit as st

# Function to render the home page content
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")

# Function to render the leaf diagnosis page content
def page_leaf(image_file):
    st.title("Leaf Diagnosis")
    st.write("Upload your image here to check the health of the leaf")
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
    st.image(load_image(image_file), width=250)
    img = Image.open(image_file)
    return img


# Dictionary mapping page names to their respective rendering functions
pages = {
    "Home": page_home,
    "About": page_leaf,
}

# Set the title and options for the sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
if selected_page in pages:
    pages[selected_page]()
