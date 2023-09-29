import streamlit as st
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
    # Add an index to the username column for faster lookups
    c.execute('CREATE INDEX IF NOT EXISTS idx_username ON users (username)')
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
    
    # Flag to determine if the user is logged in
    is_logged_in = False
    
    if st.button('Login'):
        if username and password:
            if authenticate_user(username, password):
                st.success('Login successful!')
                is_logged_in = True
            else:
                st.error('Invalid username or password. Please try again.')
        else:
            st.warning('Please enter a username and password.')
    
    conn.close()
    return is_logged_in

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
# Rest of the code remains the same ...

# Login section
# Rest of the code remains the same ...

# Render the selected page and redirect if logged in
if selected_page in pages:
    if selected_page == "Home":
        is_logged_in = page_home()
        if is_logged_in:
            # Redirect to the leaf diagnosis page
            page_leaf()
    else:
        pages[selected_page]()
