import streamlit as st
import pandas as pd
from core.detector import detect_attack
st.set_page_config(
    page_title="Agentic AI Red-Team Harness",
    page_icon="🛡️",
    layout="wide"
)

# Load attack corpus
@st.cache_data
def load_attacks():
    return pd.read_csv("data/attacks.csv")


attacks = load_attacks()

# Sidebar
st.sidebar.title("🛡️ Red-Team Harness")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Attack Simulator"
    ]
)


# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.title("🛡️ Agentic AI Red-Team Harness")

    st.subheader(
        "Prompt Injection, Tool Abuse & Data Exfiltration Testing"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Attacks",
            len(attacks)
        )

    with col2:
        st.metric(
            "Direct Injection",
            len(attacks[
                attacks["category"] == "Direct Prompt Injection"
            ])
        )

    with col3:
        st.metric(
            "Tool Abuse",
            len(attacks[
                attacks["category"] == "Tool Abuse"
            ])
        )

    with col4:
        st.metric(
            "Data Exfiltration",
            len(attacks[
                attacks["category"] == "Data Exfiltration"
            ])
        )

    st.divider()

    st.subheader("Attack Corpus")

    st.dataframe(
        attacks,
        use_container_width=True
    )


# =========================
# ATTACK SIMULATOR
# =========================

elif page == "Attack Simulator":

    st.title("🎯 Attack Simulator")

    st.write(
        "Select a synthetic attack from the red-team corpus "
        "and simulate the attack."
    )

    st.divider()

    # Category selection
    categories = attacks["category"].unique()

    selected_category = st.selectbox(
        "Select Attack Category",
        categories
    )

    # Filter attacks
    filtered_attacks = attacks[
        attacks["category"] == selected_category
    ]

    # Attack selection
    selected_id = st.selectbox(
        "Select Attack",
        filtered_attacks["id"].tolist()
    )

    attack = filtered_attacks[
        filtered_attacks["id"] == selected_id
    ].iloc[0]

    st.subheader("Attack Details")

    st.write("**Attack ID:**", attack["id"])

    st.write("**Category:**", attack["category"])

    st.write("**Severity:**", attack["severity"])

    st.write("**Target Tool:**", attack["tool"])

    st.text_area(
        "Attack Payload",
        attack["payload"],
        height=120
    )

    st.divider()

    result = None

    if st.button("Run Attack"):
        result = detect_attack(attack["payload"])

    if result is not None:
        st.subheader("Detection Result")

        if result["decision"] == "BLOCK":
            st.error("🚨 ATTACK BLOCKED")
        else:
            st.success("✅ REQUEST ALLOWED")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", result["risk_score"])

        with col2:
            st.metric("Severity", result["severity"])

        with col3:
            st.metric("Decision", result["decision"])

        st.write("### Detected Category")
        st.write(result["category"])

        st.write("### Detection Reasons")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.warning(reason)
        else:
            st.success("No suspicious behavior detected.")

        st.write("### Pattern Matches")

        if result["injection_matches"]:
            st.write(
                "Prompt Injection:",
                result["injection_matches"]
            )

        if result["tool_matches"]:
            st.write(
                "Tool Abuse:",
                result["tool_matches"]
            )

        if result["exfiltration_matches"]:
            st.write(
                "Data Exfiltration:",
                result["exfiltration_matches"]
            )