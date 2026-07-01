from pyexpat import model
##STATIC PROMPTING
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
import streamlit as st

st.header("Research Tool")
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",temperature=1.5
)
user_input = st.text_area("Enter your query here:")

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)