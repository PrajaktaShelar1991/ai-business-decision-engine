import streamlit as st
import requests

st.title("🤖 AI Business Decision Engine (Free Version)")

user_input = st.text_area("Enter Business Problem", "Revenue dropped by 15%")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def query(payload):
    try:
        response = requests.post(API_URL, json=payload)

        # Check if response is OK
        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code}"}

        return response.json()

    except Exception as e:
        return {"error": str(e)}

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

    # Handle errors safely
    if "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        try:
            output = result[0]["generated_text"]
            st.write(output)
        except:
            st.warning("Model is loading or response format changed. Please try again in a few seconds.")
