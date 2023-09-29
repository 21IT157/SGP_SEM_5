import streamlit as st
from PIL import Image
import sqlite3

# Function to render page content
def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page.")
    import streamlit as st
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users
    (username TEXT PRIMARY KEY, password TEXT)
    ''')
    conn.commit()
    def register_user(username, password):
        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            st.success('User registered successfully!')
        except sqlite3.IntegrityError:
            st.error('User already exists. Please choose a different username.')
    def authenticate_user(username, password):
        c.execute('SELECT password FROM users WHERE username = ?', (username,))
        row = c.fetchone()
        if row and row[0] == password:
            return True
        else:
            return False
    st.header('Register a new user')
    new_username = st.text_input('Enter username:')
    new_password = st.text_input('Enter password:', type='password')
    if st.button('Register'):
        if new_username and new_password:
            register_user(new_username, new_password)
        else:
            st.warning('Please enter a username and password.')
    st.header('Login')
    username = st.text_input('Enter your username:')
    password = st.text_input('Enter your password:', type='password')
    if st.button('Login'):
        if username and password:
            if authenticate_user(username, password):
                st.success('Login successful!')
            else:
                st.error('Invalid username or password. Please try again.')
        else:
            st.warning('Please enter a username and password.')
    conn.close()


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
if selected_page in pages:
    if selected_page == "Home":
        is_logged_in = page_home()
        if is_logged_in:
            # Redirect to the leaf diagnosis page
            page_leaf()
    else:
        pages[selected_page]()
