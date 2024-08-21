import streamlit as st
from datetime import datetime

# Set the title of the app
st.title("Simple Streamlit App")

# Display a welcome message
st.write("Welcome to this simple Streamlit app!")

# Create a text input for the user's name
name = st.text_input("What's your name?")

# Display a personalized greeting if the name is provided
if name:
    st.write(f"Hello, {name}! Nice to meet you.")

# Display the current date and time
st.write("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Create a button to display a message
if st.button("Click me!"):
    st.write("You clicked the button!")

# Show a sidebar with additional information
st.sidebar.title("About")
st.sidebar.write("This is a simple Streamlit app created as an example.")
