# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Configure Google Generative AI with the API key from the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize GenerativeModel with the 'gemini-pro' model
model = genai.GenerativeModel('gemini-pro')

# Function to get Gemini's response for a given question
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set Streamlit page configuration
st.set_page_config(page_title='Gemini Q&A')

# Streamlit UI
st.header("Gemini LLM Application")

# User input for asking a question
input_question = st.text_input("Input: ", key="input")

# Button to trigger question generation
submit_button = st.button("Ask the question")

# Check if the submit button is clicked
if submit_button:
    # Get Gemini's response
    response = get_gemini_response(input_question)
    
    # Display the response
    st.subheader("The Response is")
    st.write(response)
