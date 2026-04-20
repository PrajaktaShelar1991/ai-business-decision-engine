import streamlit as st

st.title("🤖 AI Business Decision Engine")

st.write("Enter a business problem and analyze it using AI agents.")

# Input
user_input = st.text_area("Enter Business Problem", "Revenue dropped by 15%")

# Button
if st.button("Run Analysis"):

    st.subheader("🧠 Problem Definition")
    st.write("Revenue decline observed. Key metrics impacted: traffic, conversion rate.")

    st.subheader("📊 Data Insights")
    st.write("Mobile traffic and conversion rates are declining significantly.")

    st.subheader("🔍 Root Cause")
    st.write("Poor mobile performance and checkout friction impacting conversions.")

    st.subheader("🧭 Strategy")
    st.write("""
    - Improve mobile performance (High)
    - Optimize checkout UX (High)
    - Run A/B tests (Medium)
    """)

    st.subheader("📄 Execution Plan (PRD + Roadmap)")
    st.write("Includes PRD, phased roadmap, and Jira tasks for implementation.")
