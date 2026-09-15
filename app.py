import streamlit as st
import pandas as pd

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

    if st.button(
        "🚀 Run Attack",
        use_container_width=True
    ):

        st.subheader("Attack Result")

        if attack["expected_action"] == "Block":

            st.error("🚨 ATTACK SHOULD BE BLOCKED")

        else:

            st.success("✅ REQUEST SHOULD BE ALLOWED")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Severity",
                attack["severity"]
            )

        with col2:
            st.metric(
                "Expected Action",
                attack["expected_action"]
            )

        with col3:
            st.metric(
                "Target Tool",
                attack["tool"]
            )

        st.info(
            "This is currently a simulated test. "
            "The actual detection engine will be implemented next."
        )