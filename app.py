
# import streamlit as st
# from PIL import Image
# def page_home():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page.")
# def page_leaf():
#     st.title("Leaf Diagnosis")
#     st.write("Upload your image to check whether the leaf is diseased or not")
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
#     if uploaded_file is not None:
#         # Display image as a preview using HTML and CSS
#         st.write("<h3>Preview Image:</h3>", unsafe_allow_html=True)
#         st.image(uploaded_file, use_column_width=True)
#         st.write("Classifying...")
# pages = {
#     "Home": page_home,
#     "Leaf Diagnosis": page_leaf,
# }
# st.sidebar.title("Navigation")
# selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# # Render the selected page
# if selected_page in pages:
#     pages[selected_page]()
import streamlit as st
from googletrans import Translator, LANGUAGES

# Function to get translations using Google Translate API
def get_translation(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Function to display the home page
def page_home():
    st.title(get_translation("Home Page", selected_language))
    st.write(get_translation("Welcome to the Home Page.", selected_language))

# Function to display the leaf diagnosis page
def page_leaf():
    st.title(get_translation("Leaf Diagnosis", selected_language))
    st.write(get_translation("Upload your image to check whether the leaf is diseased or not", selected_language))

# Language selection
languages = {value: key for key, value in LANGUAGES.items()}  # Reverse language mapping
selected_language = st.sidebar.selectbox("Select Language", list(languages.values()))

# Map the selected language to its language code (e.g., 'en', 'gu')
target_language_code = [k for k, v in LANGUAGES.items() if v == selected_language][0]

# Page selection
pages = {
    _("Home Page"): page_home,
    _("Leaf Diagnosis"): page_leaf,
}
st.sidebar.title(_("Navigation"))
selected_page = st.sidebar.radio(_("Go to"), list(pages.keys()))

# Render the selected page
if selected_page in pages:
    pages[selected_page]()
