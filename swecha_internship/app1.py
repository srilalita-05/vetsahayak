import streamlit as st
import requests

st.title("AI Story Generator Chatbot")

with st.form("story_form"):
    characters = st.text_area("Enter characters (one per line, with optional description):")
    genre = st.text_input("Genre (e.g., fantasy, sci-fi, romance):")
    setting = st.text_input("Optional setting or extra details:")
    submitted = st.form_submit_button("Generate Story")

if submitted:
    # Construct prompt based on user input
    prompt = f"Write a {genre} story with these characters: {characters}."
    if setting:
        prompt += f" Set in {setting}."
    # Send prompt to Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt}
    )
    story = response.json().get("response")
    st.write(story)

