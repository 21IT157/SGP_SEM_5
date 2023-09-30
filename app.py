
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
import sqlite3
from PIL import Image

# Connect to SQLite database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user information (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')
conn.commit()

def register_user(username, password):
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    st.success('User registered successfully.')

def login_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchall()  # Fetch all users matching the criteria
    return user

def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")
    
    st.subheader("Login")
    login_username = st.text_input('Username:')
    login_password = st.text_input('Password:', type='password')
    if st.button('Login'):
        users = login_user(login_username, login_password)
        if users:
            st.success(f'Welcome, {login_username}! Login successful.')
        else:
            st.error('Invalid username or password.')

    st.subheader("Register")
    reg_username = st.text_input('Username for registration:')
    reg_password = st.text_input('Password for registration:', type='password')
    if st.button('Register'):
        register_user(reg_username, reg_password)

def page_leaf():
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

