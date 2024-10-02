import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#for testing in your local use this method 
#groq_api_key = os.getenv("GROQ_API_KEY")

#This is for deployment through streamlit

groq_api_key = st.secrets['GROQ_API_KEY']

# Initialize the model
model = ChatGroq(
    model_name="Gemma2-9b-it",
    groq_api_key=groq_api_key
)

# Create a chat prompt template
system_template = "You are a helpful assistant that translates {input_language} to {output_language}. just give me the translated text"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

# Create a StrOutputParser
output_parser = StrOutputParser()

# Construct the chain
chain = chat_prompt | model | output_parser

# Streamlit UI
st.title("Language Translator")

input_language = st.text_input("Input Language", "English")
output_language = st.text_input("Output Language", "French")
text = st.text_area("Text to Translate", "Hello, how are you?")

if st.button("Translate"):
    with st.spinner("Translating..."):
        result = chain.invoke({
            "input_language": input_language,
            "output_language": output_language,
            "text": text
        })
        st.success("Translation complete!")
        st.write("Translated text:")
        st.write(result)

