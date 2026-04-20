import streamlit as st
import requests

st.title("🤖 AI Business Decision Engine (Free Version)")

user_input = st.text_area("Enter Business Problem", "Revenue dropped by 15%")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

if st.button("Run Analysis"):

    prompt = f"""
    You are a business analyst.

    Problem: {user_input}

    Provide:
    1. Problem Definition
    2. Data Insights
    3. Root Cause
    4. Strategy
    5. Execution Plan (PRD + Roadmap + Tasks)
    """

    result = query({"inputs": prompt})

    try:
        output = result[0]["generated_text"]
    except:
        output = "Model is loading or busy. Please try again."

    st.write(output)
