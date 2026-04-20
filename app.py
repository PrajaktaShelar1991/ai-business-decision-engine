import streamlit as st

# Page config
st.set_page_config(page_title="AI Business Decision Engine", layout="wide")

# Title
st.title("🤖 AI Business Decision Engine")
st.markdown("Analyze business problems and generate structured insights, strategy, and execution plans.")

# Dropdown for scenario
scenario = st.selectbox(
    "Select Business Scenario",
    ["Revenue Drop", "Traffic Decline", "Retention Drop"]
)

# Input
user_input = st.text_area("Enter Business Problem", "Describe the issue in detail...")

# Button
if st.button("Run Analysis"):

    st.success(f"Analysis generated for: {scenario}")

    tab1, tab2, tab3 = st.tabs(["📊 Insights", "🧭 Strategy", "📄 Execution"])

    # ================= REVENUE =================
    if scenario == "Revenue Drop":

        with tab1:
            st.subheader("🧠 Problem Definition")
            st.write("Revenue decline observed, primarily driven by mobile conversion issues.")

            st.subheader("📊 Data Insights")
            st.write("""
            - Mobile traffic declining  
            - Conversion rate dropping significantly  
            - Revenue impact aligned with mobile segment  
            """)

            st.subheader("🔍 Root Cause")
            st.write("""
            - Slow mobile performance  
            - Checkout friction  
            - Poor mobile UX  
            """)

        with tab2:
            st.subheader("🧭 Recommendations")
            st.write("""
            1. Improve mobile performance (High)  
            2. Optimize checkout UX (High)  
            3. Run A/B tests (Medium)  
            """)

            st.subheader("📈 Expected Impact")
            st.write("5–10% increase in conversion rate")

        with tab3:
            st.subheader("📄 PRD")
            st.write("Fix mobile performance and checkout flow")

            st.subheader("🗺️ Roadmap")
            st.write("""
            Phase 1: Diagnose  
            Phase 2: Optimize  
            Phase 3: Test  
            Phase 4: Monitor  
            """)

            st.subheader("✅ Tasks")
            st.write("""
            - Improve load speed  
            - Redesign checkout  
            - Run experiments  
            """)

    # ================= TRAFFIC =================
    elif scenario == "Traffic Decline":

        with tab1:
            st.subheader("🧠 Problem Definition")
            st.write("Traffic decline observed across key acquisition channels.")

            st.subheader("📊 Data Insights")
            st.write("""
            - Organic traffic dropping  
            - Paid campaigns underperforming  
            - Lower impressions and clicks  
            """)

            st.subheader("🔍 Root Cause")
            st.write("""
            - SEO ranking drop  
            - Ineffective ad targeting  
            - Reduced marketing spend  
            """)

        with tab2:
            st.subheader("🧭 Recommendations")
            st.write("""
            1. Improve SEO strategy (High)  
            2. Optimize ad campaigns (High)  
            3. Increase marketing investment (Medium)  
            """)

            st.subheader("📈 Expected Impact")
            st.write("10–20% increase in traffic")

        with tab3:
            st.subheader("📄 PRD")
            st.write("Improve acquisition channels and visibility")

            st.subheader("🗺️ Roadmap")
            st.write("""
            Phase 1: Audit traffic sources  
            Phase 2: Optimize campaigns  
            Phase 3: Scale channels  
            """)

            st.subheader("✅ Tasks")
            st.write("""
            - SEO audit  
            - Campaign optimization  
            - Budget allocation  
            """)

    # ================= RETENTION =================
    elif scenario == "Retention Drop":

        with tab1:
            st.subheader("🧠 Problem Definition")
            st.write("User retention declining after initial engagement.")

            st.subheader("📊 Data Insights")
            st.write("""
            - High churn rate  
            - Drop after first session  
            - Low repeat usage  
            """)

            st.subheader("🔍 Root Cause")
            st.write("""
            - Poor onboarding experience  
            - Lack of engagement features  
            - Low perceived value  
            """)

        with tab2:
            st.subheader("🧭 Recommendations")
            st.write("""
            1. Improve onboarding (High)  
            2. Add engagement features (High)  
            3. Personalize user experience (Medium)  
            """)

            st.subheader("📈 Expected Impact")
            st.write("15–25% improvement in retention")

        with tab3:
            st.subheader("📄 PRD")
            st.write("Enhance onboarding and engagement")

            st.subheader("🗺️ Roadmap")
            st.write("""
            Phase 1: Analyze churn  
            Phase 2: Improve onboarding  
            Phase 3: Add features  
            """)

            st.subheader("✅ Tasks")
            st.write("""
            - Redesign onboarding  
            - Add notifications  
            - Build engagement loops  
            """)

# Footer
st.markdown("---")
st.markdown("Built as part of AI Product Management Portfolio 🚀")
