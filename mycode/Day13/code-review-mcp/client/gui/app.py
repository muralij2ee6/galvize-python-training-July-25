import streamlit as st
import requests

st.title("GitLab Code Reviewer 🛠️")

# Sample GitLab project selector
project = st.selectbox(
    "Select sample project",
    ["Python Microservice", "React Frontend", "Go CLI Tool"]
)

# Load sample code
with open(f"test_data/{project}.txt") as f:
    code = f.read()

if st.button("Review Code"):
    try:
        response = requests.post(
            "http://server:8000/review",  # Note: using service name instead of localhost
            json={"code": code, "language": project.split()[0]}
        )
        response.raise_for_status()  # Raises an exception for 4XX/5XX errors
        st.json(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the server: {e}")
