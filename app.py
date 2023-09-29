import streamlit as st
from PIL import Image

st.title("Upload and Preview Image")

import streamlit as st
from PIL import Image
# Function to render page content
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")

def page_about():
    st.title("Leaf Diagnosis")
    st.write("Upload your image to check whether the leaf is diseased or not")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Display image as a preview using HTML and CSS
        st.write("<h3>Preview Image:</h3>", unsafe_allow_html=True)
        st.image(uploaded_file, use_column_width=True)
        st.write("Classifying...")
pages = {
    "Home": page_home,
    "Leaf Diagnosis": page_leaf,
}
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
if selected_page in pages:
    pages[selected_page]()
