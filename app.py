import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="AI Business Decision Engine", layout="wide")

# Title
st.title("🤖 AI Business Decision Engine")
st.markdown("Analyze business problems with insights, charts, and execution plans.")

# Dropdown
scenario = st.selectbox(
    "Select Business Scenario",
    ["Revenue Drop", "Traffic Decline", "Retention Drop"]
)

# Input
user_input = st.text_area("Enter Business Problem", "Describe the issue...")

# Sample data (mock dataset)
data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Traffic": [1000, 950, 900, 1100, 850],
    "Conversion": [5.0, 4.8, 4.5, 5.2, 4.2],
    "Retention": [70, 68, 65, 72, 60]
})

# Button
if st.button("Run Analysis"):

    st.success(f"Analysis generated for: {scenario}")

    tab1, tab2, tab3 = st.tabs(["📊 Insights", "🧭 Strategy", "📄 Execution"])

    # -------- INSIGHTS --------
    with tab1:

        st.subheader("📈 Trend Analysis")

        fig, ax = plt.subplots()

        if scenario == "Revenue Drop":
            ax.plot(data["Day"], data["Conversion"])
            ax.set_title("Conversion Rate Trend")

        elif scenario == "Traffic Decline":
            ax.plot(data["Day"], data["Traffic"])
            ax.set_title("Traffic Trend")

        elif scenario == "Retention Drop":
            ax.plot(data["Day"], data["Retention"])
            ax.set_title("Retention Trend")

        st.pyplot(fig)

        st.subheader("🔍 Key Insights")

        if scenario == "Revenue Drop":
            st.write("""
            - Conversion rate declining mid-week  
            - Revenue drop linked to mobile performance  
            """)

        elif scenario == "Traffic Decline":
            st.write("""
            - Traffic steadily decreasing  
            - Acquisition channels underperforming  
            """)

        elif scenario == "Retention Drop":
            st.write("""
            - Retention drops significantly towards end  
            - Users not returning after first session  
            """)

    # -------- STRATEGY --------
    with tab2:

        if scenario == "Revenue Drop":
            st.write("""
            - Improve mobile performance (High)  
            - Optimize checkout UX (High)  
            """)

        elif scenario == "Traffic Decline":
            st.write("""
            - Improve SEO (High)  
            - Optimize ad campaigns (High)  
            """)

        elif scenario == "Retention Drop":
            st.write("""
            - Improve onboarding (High)  
            - Add engagement features (High)  
            """)

    # -------- EXECUTION --------
    with tab3:

        st.subheader("📄 Execution Plan")

        st.write("""
        Phase 1: Diagnose issue  
        Phase 2: Implement fixes  
        Phase 3: Test & optimize  
        """)

# Footer
st.markdown("---")
st.markdown("Built as part of AI Product Management Portfolio 🚀")
