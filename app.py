# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI with API key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# Initialize GenerativeModel with the 'gemini-pro' model
model = genai.GenerativeModel('gemini-pro')

# Main Streamlit UI
st.set_page_config(
    page_title='Gemini Q&A',
    page_icon='✨',
    layout='wide'
)

# Page title
st.title("Gemini LLM Application")

# User input for asking a question
input_question = st.text_input("Ask a question:")

# Button to trigger question generation
if st.button("Get Response"):
    # Check if the user entered a question
    if not input_question:
        st.warning("Please enter a question.")
    else:
        # Show a loading spinner while generating the response
        with st.spinner("Generating Response..."):
            # Generate response from Gemini
            response = model.generate_content(input_question).text
        # Display Gemini's response
        st.subheader("Gemini's Response:")
        st.write(response)
