import streamlit as st
import requests
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Study Chatbot", layout="centered")
st.title("📚 AI Study Chatbot")

API_BASE_URL = os.getenv("API_BASE_URL")
USER_ID = os.getenv("USER_ID")

def query_skillcaptain(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"{API_BASE_URL}?userId={USER_ID}&prompt={encoded_prompt}"
        response = requests.get(url, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            return response.text
        else:
            return f"API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception: {str(e)}"


mode = st.sidebar.selectbox("Choose a mode", ["Ask a Question", "Summarize Notes", "Generate MCQs"])

if mode == "Ask a Question":
    question = st.text_area("Enter your question:")
    if st.button("Get Answer"):
        if question.strip():
            prompt = question.strip()
            result = query_skillcaptain(prompt)
            st.success("Answer:")
            st.write(result)

elif mode == "Summarize Notes":
    notes = st.text_area("Paste your notes:")
    if st.button("Summarize"):
        if notes.strip():
            prompt = f"Summarize the following notes:\n{notes.strip()}"
            result = query_skillcaptain(prompt)
            st.success("Summary:")
            st.write(result)

elif mode == "Generate MCQs":
    topic = st.text_input("Enter a topic for MCQs:")
    if st.button("Generate"):
        if topic.strip():
            prompt = f"Generate 3 multiple choice questions (with answers) on the topic: {topic.strip()}"
            result = query_skillcaptain(prompt)
            st.success("Generated MCQs:")
            st.write(result)