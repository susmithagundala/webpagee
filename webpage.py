pip install streamlit
import streamlit as st

# Set the title of the app
st.title('My First Streamlit Web Page')

# Add a header
st.header('Welcome to My Streamlit App')

# Add a text
st.write('This is a simple web page created using Streamlit.')

# Add a sidebar with a text input
name = st.sidebar.text_input('Enter your name:', '')

# Add a slider
age = st.slider('Select your age:', 0, 100, 25)

# Display the input
if name:
    st.write(f'Hello, {name}! You are {age} years old.')

# Add a checkbox
if st.checkbox('Show Secret Message'):
    st.write('You found the secret message!')

# Add an image (optional)
st.image('https://via.placeholder.com/150', caption='Sample Image')

# Add a button
if st.button('Click Me'):
    st.write('Button Clicked!')
streamlit run app.py
