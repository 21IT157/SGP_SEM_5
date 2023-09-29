# import streamlit as st
# from PIL import Image

# st.title("Upload and Preview Image")

# # Upload image through Streamlit
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# # Display a preview of the image
# if uploaded_file is not None:
#     # Display image as a preview using HTML and CSS
#     st.write("<h3>Preview Image:</h3>", unsafe_allow_html=True)
#     st.image(uploaded_file, use_column_width=True)

#     # You can also use Pillow to display the preview
#     # img = Image.open(uploaded_file)
#     # st.image(img, caption="Preview Image", use_column_width=True)
    
#     st.write("Classifying...")

#     # Perform any processing or analysis on the uploaded image if needed
#     # For example, you can use a machine learning model to classify the image
#     # ...

#     # Display additional information or results based on the image analysis
#     # For example, you can display the image class or any other relevant information
#     # ...
import streamlit as st

# Function to render page content
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")

def page_about():
    st.title("About Page")
    st.write("This is the About Page.")

def page_contact():
    st.title("Contact Page")
    st.write("This is the Contact Page.")

# Page navigation
pages = {
    "Home": page_home,
    "About": page_about,
    "Contact": page_contact,
}

# Streamlit app
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
if selected_page in pages:
    pages[selected_page]()
