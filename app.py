import streamlit as st
from PIL import Image
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table to store user information with proper indexing
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          username TEXT UNIQUE, password TEXT)
          ''')
conn.commit()

# Function to register a new user
def register_user(username, password):
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        st.success('User registered successfully!')
    except sqlite3.IntegrityError:
        st.error('User already exists. Please choose a different username.')

# Function to authenticate a user
def authenticate_user(username, password):
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = c.fetchone()
    if row and row[0] == password:
        return True
    else:
        return False

# Function to render the leaf diagnosis page
def page_leaf():
    st.title("Leaf Diagnosis")
    st.write("Upload your image to check whether the leaf is diseased or not")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Display image as a preview using HTML and CSS
        st.write("<h3>Preview Image:</h3>", unsafe_allow_html=True)
        st.image(uploaded_file, use_column_width=True)
        st.write("Classifying...")

# Streamlit app
st.title('User Authentication and Leaf Diagnosis App')

# Registration section
st.header('Register a new user')
new_username = st.text_input('Enter username:')
new_password = st.text_input('Enter password:', type='password')
if st.button('Register'):
    if new_username and new_password:
        register_user(new_username, new_password)
    else:
        st.warning('Please enter a username and password.')

# Login section
st.header('Login')
username = st.text_input('Enter your username:')
password = st.text_input('Enter your password:', type='password')

if st.button('Login'):
    if username and password:
        if authenticate_user(username, password):
            st.success('Login successful!')
            st.write("Redirecting to Leaf Diagnosis page...")
            page_leaf()  # Redirect to the leaf diagnosis page
        else:
            st.error('Invalid username or password. Please try again.')
    else:
        st.warning('Please enter a username and password.')

# Close the database connection
conn.close()
