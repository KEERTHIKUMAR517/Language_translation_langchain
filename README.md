# Language Translator

This is a Streamlit-based web application that uses the Groq API to translate text from one language to another.

## Features

- Translate text between any two languages
- Simple and intuitive user interface
- Powered by Groq's language model

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Groq API key. If not, sign up at [Groq's website](https://www.groq.com) to obtain one.
- You have Python 3.7+ installed on your system.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/KEERTHIKUMAR517/language-translator.git
   cd language-translator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run serve_streamlit.py
   ```

2. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

3. Use the application:
   - Enter the input language (e.g., "English")
   - Enter the output language (e.g., "French")
   - Type or paste the text you want to translate
   - Click the "Translate" button

4. The translated text will appear below the input fields.

## File Structure

- `serve_streamlit.py`: The main Streamlit application file
- `requirements.txt`: List of Python dependencies
- `.env`: Environment file for storing the Groq API key (not included in the repository)
- `README.md`: This file, containing project information and instructions

## Deployment

To deploy this application:

1. Ensure all files are in place, including `serve_streamlit.py`, `requirements.txt`, and `.env` (with your API key).

2. Choose a hosting platform that supports Streamlit applications (e.g., Streamlit Sharing, Heroku, or Google Cloud Platform).

3. Follow the hosting platform's instructions for deploying a Streamlit app, ensuring you set up the environment variable for your Groq API key.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project uses the Groq API for language translation.
- Built with Streamlit and LangChain.
