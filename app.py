import streamlit as st

st.set_page_config(
    page_title="Agentic AI Red-Team Harness",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Agentic AI Red-Team Harness")

st.subheader("Prompt Injection, Tool Abuse & Data Exfiltration Testing")

st.info(
    "A safe local environment for testing AI-agent security "
    "using synthetic data and mock tools."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tests", 0)

with col2:
    st.metric("Blocked Attacks", 0)

with col3:
    st.metric("Data Leaks", 0)

st.divider()

st.subheader("System Status")

st.success("Application is running")

st.write(
    "Day 1 prototype successfully initialized."
)