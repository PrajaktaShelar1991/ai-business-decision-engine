import csv
import streamlit as st


st.set_page_config(page_title="AI Business Decision Engine", layout="wide")


def load_csv(path: str):
    with open(path, "r", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def append_csv_row(path: str, row: dict):
    with open(path, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=row.keys())
        writer.writerow(row)


def to_float(value: str) -> float:
    return float(value.replace("%", "").strip())


def show_key_number(title: str, value: str, help_text: str = ""):
    st.metric(title, value, help=help_text or None)


def normalize_field_value(field_name: str, value: str) -> str:
    clean_value = value.strip()
    percent_fields = {"PaidCTR", "TopFunnelCVR", "DropAtStage", "ReasonShare"}
    if field_name in percent_fields and clean_value and not clean_value.endswith("%"):
        return f"{clean_value}%"
    return clean_value


def validate_row(row: dict, numeric_fields: set, percent_fields: set):
    errors = []

    for field, value in row.items():
        if not value.strip():
            errors.append(f"`{field}` cannot be empty.")

    for field in numeric_fields:
        value = row[field].strip()
        if not value:
            continue
        try:
            float(value)
        except ValueError:
            errors.append(f"`{field}` must be a number.")

    for field in percent_fields:
        value = row[field].strip()
        if not value:
            continue
        if not value.endswith("%"):
            errors.append(f"`{field}` must end with `%`.")
            continue
        try:
            float(value.replace("%", ""))
        except ValueError:
            errors.append(f"`{field}` must contain a valid percentage.")

    return errors


def render_data_manager():
    st.subheader("Data Manager")
    st.caption("Add realistic rows to any dataset and save them permanently to CSV.")

    dataset_configs = {
        "Revenue": {
            "path": "sample-data/revenue_data.csv",
            "fields": [
                "Date",
                "Traffic",
                "ConversionRate",
                "Revenue",
                "Device",
                "PageLoadSec",
                "CheckoutDropoffPct",
                "AOV",
            ],
            "numeric_fields": {
                "Traffic",
                "ConversionRate",
                "Revenue",
                "PageLoadSec",
                "CheckoutDropoffPct",
                "AOV",
            },
            "percent_fields": set(),
            "hints": {
                "Date": "Format: YYYY-MM-DD",
                "Traffic": "Example: 9500",
                "ConversionRate": "Example: 2.7",
                "Revenue": "Example: 112000",
                "Device": "Example: Mobile or Desktop",
                "PageLoadSec": "Example: 3.2",
                "CheckoutDropoffPct": "Example: 59",
                "AOV": "Example: 410",
            },
        },
        "Acquisition": {
            "path": "sample-data/acquisition_data.csv",
            "fields": [
                "Week",
                "OrganicSessions",
                "PaidSessions",
                "PaidCTR",
                "CAC",
                "TopFunnelCVR",
                "Notes",
            ],
            "numeric_fields": {"OrganicSessions", "PaidSessions", "CAC"},
            "percent_fields": {"PaidCTR", "TopFunnelCVR"},
            "hints": {
                "Week": "Format: YYYY-W##",
                "OrganicSessions": "Example: 32500",
                "PaidSessions": "Example: 14300",
                "PaidCTR": "Example: 1.8%",
                "CAC": "Example: 44",
                "TopFunnelCVR": "Example: 3.9%",
                "Notes": "Short context note",
            },
        },
        "Dropout": {
            "path": "sample-data/dropout_data.csv",
            "fields": [
                "Stage",
                "UsersAtStage",
                "DropAtStage",
                "TopReason",
                "ReasonShare",
                "Signal",
            ],
            "numeric_fields": {"UsersAtStage"},
            "percent_fields": {"DropAtStage", "ReasonShare"},
            "hints": {
                "Stage": "Example: Week 2 Retained",
                "UsersAtStage": "Example: 4300",
                "DropAtStage": "Example: 15%",
                "TopReason": "Primary reason for dropout",
                "ReasonShare": "Example: 22%",
                "Signal": "Observed behavioral signal",
            },
        },
    }

    dataset_name = st.selectbox(
        "Choose dataset",
        list(dataset_configs.keys()),
        key="data_manager_dataset",
    )
    config = dataset_configs[dataset_name]

    with st.form(key=f"{dataset_name.lower()}_data_form"):
        form_values = {}
        for field in config["fields"]:
            form_values[field] = st.text_input(
                field,
                value="",
                help=config["hints"].get(field, ""),
            )

        submitted = st.form_submit_button("Add row")

    if submitted:
        normalized_row = {
            field: normalize_field_value(field, value)
            for field, value in form_values.items()
        }
        errors = validate_row(
            normalized_row,
            numeric_fields=config["numeric_fields"],
            percent_fields=config["percent_fields"],
        )

        if errors:
            for error in errors:
                st.error(error)
        else:
            append_csv_row(config["path"], normalized_row)
            st.success(f"Row added to `{config['path']}`")

    st.markdown("**Latest rows**")
    st.dataframe(load_csv(config["path"])[-8:], use_container_width=True)


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

analysis_tab, data_manager_tab = st.tabs(["Analysis", "Data Manager"])

with analysis_tab:
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

with data_manager_tab:
    render_data_manager()

st.markdown("---")
st.caption("Built as part of AI Product Management Portfolio")
