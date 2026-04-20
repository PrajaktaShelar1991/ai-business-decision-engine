import streamlit as st

# Page config
st.set_page_config(page_title="AI Business Decision Engine", layout="wide")

# Title
st.title("🤖 AI Business Decision Engine")
st.markdown("Analyze business problems and generate structured insights, strategy, and execution plans.")

# Input
user_input = st.text_area("Enter Business Problem", "Revenue dropped by 15% on mobile")

# Button
if st.button("Run Analysis"):

    st.success("Analysis generated successfully!")

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📊 Insights", "🧭 Strategy", "📄 Execution"])

    # -------- INSIGHTS TAB --------
    with tab1:
        if "revenue" in user_input.lower():

            st.subheader("🧠 Problem Definition")
            st.write("Revenue decline observed, primarily driven by drop in mobile conversions.")

            st.subheader("📊 Data Insights")
            st.write("""
            - Mobile traffic declining over time  
            - Conversion rates significantly lower on mobile vs desktop  
            - Revenue drop aligned with mobile performance issues  
            """)

            st.subheader("🔍 Root Cause")
            st.write("""
            - Slow mobile page load time  
            - Friction in checkout flow  
            - Poor mobile user experience  
            """)

        else:
            st.write("General business problem detected. Insights will vary based on scenario.")

    # -------- STRATEGY TAB --------
    with tab2:
        if "revenue" in user_input.lower():

            st.subheader("🧭 Recommendations")
            st.write("""
            1. Improve mobile performance (High Priority)  
            2. Optimize checkout experience (High Priority)  
            3. Conduct A/B testing for UX improvements (Medium Priority)  
            4. Improve page load speed (High Priority)  
            """)

            st.subheader("📈 Expected Impact")
            st.write("""
            - Conversion increase: 5–10%  
            - Revenue recovery within 4–6 weeks  
            """)

        else:
            st.write("Strategy will be generated based on the type of problem.")

    # -------- EXECUTION TAB --------
    with tab3:
        if "revenue" in user_input.lower():

            st.subheader("📄 Product Requirement Document (PRD)")

            st.markdown("### Problem")
            st.write("Revenue decline due to poor mobile performance and conversion issues.")

            st.markdown("### Solution")
            st.write("""
            - Optimize mobile speed  
            - Improve checkout UX  
            - Reduce friction in payment flow  
            """)

            st.markdown("### Metrics")
            st.write("""
            - Conversion rate  
            - Page load time  
            - Revenue growth  
            """)

            st.markdown("### 🗺️ Roadmap")
            st.write("""
            **Phase 1:** Diagnose mobile issues  
            **Phase 2:** Implement performance improvements  
            **Phase 3:** Run A/B tests  
            **Phase 4:** Monitor and optimize  
            """)

            st.markdown("### ✅ Jira Tasks")
            st.write("""
            - TASK-001: Analyze mobile performance  
            - TASK-002: Optimize frontend load time  
            - TASK-003: Redesign checkout flow  
            - TASK-004: Conduct A/B testing  
            """)

        else:
            st.write("Execution plan will be generated based on the scenario.")

# Footer
st.markdown("---")
st.markdown("Built as part of AI Product Management Portfolio 🚀")
