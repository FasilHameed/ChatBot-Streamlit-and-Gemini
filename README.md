# Gemini LLM Application

This Streamlit application utilizes the Google Generative AI language model (Gemini) to provide responses to user queries.

## Project Structure

```plaintext
gemini-llm-app/
|-- .env
|-- app.py
|-- requirements.txt
|-- README.md
|-- venv/  (Virtual Environment - optional)
|-- LICENSE


# Gemini LLM Application

This Streamlit application utilizes the Google Generative AI language model (Gemini) to provide responses to user queries.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gemini-llm-app.git
    cd gemini-llm-app
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
    ```

3. Create a `.env` file in the project root with your Google API key:

    ```dotenv
    GOOGLE_API_KEY='YOUR_GOOGLE_API_KEY'
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Open your browser and go to [http://localhost:8501](http://localhost:8501) to interact with the Gemini LLM Application.

### Dummy Link
Find the deployed version of the app [here](https://your-dummy-link.com).

## Notes
- Make sure to replace 'YOUR_GOOGLE_API_KEY' in the `.env` file with your actual Google API key.
- Update the dummy link in the README with the actual link once the app is deployed.

## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
