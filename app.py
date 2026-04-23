import csv
from pathlib import Path
import streamlit as st


st.set_page_config(page_title="AI Business Decision Engine", layout="wide")


def load_csv(path: str):
    with open(path, "r", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def to_float(value: str) -> float:
    return float(value.replace("%", "").strip())


def show_key_number(title: str, value: str, help_text: str = ""):
    st.metric(title, value, help=help_text or None)


def render_dropout_funnel(stages):
    st.subheader("Dropout Funnel")
    max_users = max(stage["users"] for stage in stages)
    for stage in stages:
        pct_of_entry = (stage["users"] / max_users) * 100
        st.write(
            f"**{stage['stage']}** - {stage['users']} users "
            f"({stage['drop_rate']} drop at this stage)"
        )
        st.progress(int(pct_of_entry))


def render_reason_attribution(reasons):
    st.subheader("Why Users Drop Out (Root Cause Attribution)")
    for reason in reasons:
        st.write(
            f"**{reason['reason']}** - contributes **{reason['share']}** of total dropouts. "
            f"Signal: {reason['signal']}"
        )


def render_scenario_revenue():
    data = load_csv("sample-data/revenue_data.csv")
    current = data[-1]
    baseline = data[0]

    traffic_drop = ((to_float(current["Traffic"]) - to_float(baseline["Traffic"])) / to_float(baseline["Traffic"])) * 100
    conversion_drop = ((to_float(current["ConversionRate"]) - to_float(baseline["ConversionRate"])) / to_float(baseline["ConversionRate"])) * 100
    revenue_drop = ((to_float(current["Revenue"]) - to_float(baseline["Revenue"])) / to_float(baseline["Revenue"])) * 100

    col1, col2, col3 = st.columns(3)
    with col1:
        show_key_number("Traffic Trend", f"{traffic_drop:.1f}%")
    with col2:
        show_key_number("Conversion Trend", f"{conversion_drop:.1f}%")
    with col3:
        show_key_number("Revenue Trend", f"{revenue_drop:.1f}%")

    st.subheader("Insight Narrative")
    st.write(
        "Revenue decline is mostly conversion-led, not pure traffic-led. "
        "Mobile sessions remain meaningful, but conversion drops after slow page loads "
        "and increased checkout drop-off."
    )

    st.subheader("Evidence")
    st.dataframe(data[-10:], use_container_width=True)

    st.subheader("Recommended Actions")
    st.markdown(
        "- Prioritize mobile performance fixes in PDP and checkout.\n"
        "- Reduce checkout fields and add express payment options.\n"
        "- Monitor by device weekly and rerun conversion experiments."
    )


def render_scenario_traffic():
    data = load_csv("sample-data/acquisition_data.csv")
    latest = data[-1]

    col1, col2, col3 = st.columns(3)
    with col1:
        show_key_number("Organic Sessions", latest["OrganicSessions"])
    with col2:
        show_key_number("Paid CTR", latest["PaidCTR"])
    with col3:
        show_key_number("CAC", latest["CAC"])

    st.subheader("Insight Narrative")
    st.write(
        "Traffic loss starts in top-of-funnel channels. Organic sessions and ad click-through "
        "have both dropped while CAC increased, indicating weaker traffic quality and targeting."
    )

    st.subheader("Evidence")
    st.dataframe(data[-10:], use_container_width=True)

    st.subheader("Recommended Actions")
    st.markdown(
        "- Recover ranking for high-intent SEO pages first.\n"
        "- Refresh paid creative and retarget high-converting audiences.\n"
        "- Shift spend from low-CTR to high-intent campaigns."
    )


def render_scenario_retention():
    data = load_csv("sample-data/dropout_data.csv")

    entry_users = int(data[0]["UsersAtStage"])
    final_users = int(data[-1]["UsersAtStage"])
    total_dropout = entry_users - final_users
    dropout_rate = (total_dropout / entry_users) * 100

    col1, col2, col3 = st.columns(3)
    with col1:
        show_key_number("Users Entered", str(entry_users))
    with col2:
        show_key_number("Users Retained", str(final_users))
    with col3:
        show_key_number("Total Dropout", f"{dropout_rate:.1f}%")

    stages = [
        {
            "stage": row["Stage"],
            "users": int(row["UsersAtStage"]),
            "drop_rate": row["DropAtStage"],
        }
        for row in data
    ]

    reasons = [
        {
            "reason": row["TopReason"],
            "share": row["ReasonShare"],
            "signal": row["Signal"],
        }
        for row in data
        if row["TopReason"]
    ]

    render_dropout_funnel(stages)
    render_reason_attribution(reasons)

    st.subheader("Clear Diagnosis")
    st.markdown(
        "- **Largest dropout stage:** Activation to first value.\n"
        "- **Main reason:** Users do not complete setup due to complexity and delayed value.\n"
        "- **Secondary reason:** Weak habit loop after week 1, especially for low-frequency users.\n"
        "- **Most affected segment:** New SMB users with no guided onboarding."
    )

    st.subheader("Recommended Actions")
    st.markdown(
        "1. Add role-based onboarding checklist with progress milestones.\n"
        "2. Trigger activation nudges within first 48 hours based on incomplete steps.\n"
        "3. Launch a week-1 value campaign with personalized use-case examples.\n"
        "4. Add success playbook for SMB segment to reduce early confusion."
    )

    st.subheader("Evidence")
    st.dataframe(data, use_container_width=True)


st.title("AI Business Decision Engine")
st.markdown(
    "Get a clearer, data-backed explanation of business performance issues and dropout drivers."
)

with st.sidebar:
    st.header("How to use")
    st.markdown(
        "1. Select a scenario.\n"
        "2. Add your business context.\n"
        "3. Run analysis to view data, diagnosis, and actions."
    )

scenario = st.selectbox(
    "Choose a scenario",
    ["Revenue Drop", "Traffic Decline", "Retention Drop"],
)
user_input = st.text_area(
    "Business context",
    "Example: New users are signing up, but many leave before seeing value.",
)

if st.button("Run Analysis", type="primary"):
    st.success(f"Generated analysis for: {scenario}")
    st.caption(f"Input context: {user_input}")

    insights_tab, strategy_tab, execution_tab = st.tabs(
        ["Insights", "Strategy", "Execution Plan"]
    )

    with insights_tab:
        if scenario == "Revenue Drop":
            render_scenario_revenue()
        elif scenario == "Traffic Decline":
            render_scenario_traffic()
        else:
            render_scenario_retention()

    with strategy_tab:
        st.subheader("Prioritization Framework")
        st.markdown(
            "- **High impact / low effort:** Quick fixes with immediate KPI movement.\n"
            "- **High impact / high effort:** Core product or platform improvements.\n"
            "- **Low impact:** Defer unless supporting larger initiatives."
        )
        st.subheader("Success Metrics")
        st.markdown(
            "- Week 1: Early leading indicators (activation, CTR, checkout completion).\n"
            "- Week 2-4: Lagging business outcomes (retention, revenue, CAC efficiency)."
        )

    with execution_tab:
        st.subheader("30-60-90 Day Plan")
        st.markdown(
            "- **0-30 days:** Instrumentation cleanup, baseline measurement, quick wins.\n"
            "- **31-60 days:** Launch experiments, monitor segment-level movement.\n"
            "- **61-90 days:** Scale proven solutions and sunset low-impact work."
        )
        st.subheader("Delivery Checklist")
        st.markdown(
            "- Define owner for each metric.\n"
            "- Set weekly insight review.\n"
            "- Document experiment outcomes.\n"
            "- Decide scale or rollback based on evidence."
        )

st.markdown("---")
st.caption("Built as part of AI Product Management Portfolio")
