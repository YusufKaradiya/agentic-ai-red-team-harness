import streamlit as st
import pandas as pd
from core.defense import apply_defense
from core.detector import detect_indirect_injection
from core.permissions import check_tool_permission
from core.leakage_guard import detect_sensitive_data
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
        "Attack Simulator",
        "Indirect Injection",
        "Tool Sandbox",
        "Output Guard",
        "Security Policy"
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

        result = apply_defense(attack["payload"])

    if result is not None:
        st.subheader("Security Decision")

        if result["decision"] == "BLOCK":
            st.error("🚨 REQUEST BLOCKED")
        else:
            st.success("✅ REQUEST ALLOWED")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Risk Score",
                result["risk_score"]
            )

        with col2:
            st.metric(
                "Severity",
                result["severity"]
            )

        with col3:
            st.metric(
                "Decision",
                result["decision"]
            )

        st.write("### Category")
        st.write(result["category"])

        st.write("### Security Action")
        st.info(result["action"])

        st.write("### Reasons")

        if result["reasons"]:

            for reason in result["reasons"]:
                st.warning(reason)

        else:
            st.success(
                "No suspicious behavior detected."
            )
elif page == "Indirect Injection":

    st.title("📄 Indirect Prompt Injection")

    st.write(
        "This module tests whether malicious instructions "
        "hidden inside external documents can be detected."
    )

    st.divider()

    document_folder = "data/documents"

    documents = [
        "safe_report.txt",
        "malicious_report.txt",
        "customer_notes.txt",
        "support_ticket.txt",
        "product_notes.txt"
    ]

    selected_document = st.selectbox(
        "Select Document",
        documents
    )

    document_path = (
        f"{document_folder}/{selected_document}"
    )

    with open(
        document_path,
        "r",
        encoding="utf-8"
    ) as file:

        document_text = file.read()

    st.subheader("Document Content")

    st.code(
        document_text,
        language="text"
    )

    st.divider()

    if st.button(
        "🔍 Scan Document",
        use_container_width=True
    ):

        result = detect_indirect_injection(
            document_text
        )

        st.subheader("Security Result")

        if result["decision"] == "BLOCK":

            st.error(
                "🚨 MALICIOUS DOCUMENT CONTENT DETECTED"
            )

        else:

            st.success(
                "✅ DOCUMENT CONTENT APPEARS SAFE"
            )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Risk Score",
                result["risk_score"]
            )

        with col2:

            st.metric(
                "Severity",
                result["severity"]
            )

        with col3:

            st.metric(
                "Decision",
                result["decision"]
            )

        st.divider()

        st.subheader("Detected Category")

        st.info(
            result["category"]
        )

        st.subheader("Detection Reasons")

        if result["reasons"]:

            for reason in result["reasons"]:

                st.warning(
                    f"⚠️ {reason}"
                )

        else:

            st.success(
                "No suspicious instructions detected."
            )

        st.divider()

        st.subheader(
            "Security Interpretation"
        )

        if result["decision"] == "BLOCK":

            st.write(
                "The document contains instructions that "
                "appear to manipulate the AI agent or request "
                "sensitive information. The content should "
                "not be trusted as an instruction source."
            )

        else:

            st.write(
                "No known malicious instruction pattern "
                "was detected in this document."
            )
elif page == "Tool Sandbox":

    st.title("🧰 Tool Permission Sandbox")

    st.write(
        "This module simulates tool authorization for "
        "a tool-enabled AI agent."
    )

    st.warning(
        "All tools are simulated. No real database, "
        "email service or external API is used."
    )

    st.divider()

    tools = [
        "Calculator",
        "File Reader",
        "Customer Database",
        "Email Sender"
    ]

    selected_tool = st.selectbox(
        "Select Tool",
        tools
    )

    st.divider()

    st.subheader("Permission Check")

    permission = check_tool_permission(
        selected_tool
    )

    if permission["allowed"]:

        st.success(
            "✅ TOOL AUTHORIZED"
        )

    else:

        st.error(
            "🚨 TOOL ACCESS BLOCKED"
        )

    st.write(
        f"**Tool:** {selected_tool}"
    )

    st.write(
        f"**Reason:** {permission['reason']}"
    )

    st.divider()

    st.subheader("Tool Permission Matrix")

    permission_data = []

    for tool in tools:

        result = check_tool_permission(tool)

        permission_data.append(
            {
                "Tool": tool,
                "Permission": (
                    "ALLOW"
                    if result["allowed"]
                    else "BLOCK"
                ),
                "Reason": result["reason"]
            }
        )

    permission_df = pd.DataFrame(
        permission_data
    )

    st.dataframe(
        permission_df,
        use_container_width=True,
        hide_index=True
    )
elif page == "Output Guard":

    st.title("🔒 Sensitive Data Output Guard")

    st.write(
        "This module checks AI or tool output for "
        "synthetic sensitive information before "
        "the response is returned to the user."
    )

    st.warning(
        "Only synthetic test data is used in this prototype."
    )

    st.divider()

    st.subheader("Test Output")

    output_text = st.text_area(
        "Enter simulated AI/tool output",
        height=180,
        placeholder=(
            "Example: The API key is "
            "SYNTHETIC_API_KEY_12345"
        )
    )

    if st.button(
        "🔍 Scan Output",
        use_container_width=True
    ):

        if not output_text.strip():

            st.warning(
                "Please enter some output to scan."
            )

        else:

            result = detect_sensitive_data(
                output_text
            )

            st.divider()

            st.subheader("Security Result")

            if result["leak_detected"]:

                st.error(
                    "🚨 SENSITIVE DATA LEAK DETECTED"
                )

            else:

                st.success(
                    "✅ NO SENSITIVE DATA DETECTED"
                )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Leak Detected",
                    "YES"
                    if result["leak_detected"]
                    else "NO"
                )

            with col2:

                st.metric(
                    "Risk Score",
                    result["risk_score"]
                )

            with col3:

                st.metric(
                    "Decision",
                    result["decision"]
                )

            st.divider()

            st.subheader("Detection Findings")

            if result["findings"]:

                for finding in result["findings"]:

                    st.warning(
                        f"⚠️ {finding}"
                    )

            else:

                st.success(
                    "No sensitive information was found."
                )

            st.divider()

            st.subheader("Output Handling")

            if result["decision"] == "BLOCK":

                st.error(
                    "The output should be blocked and "
                    "must not be returned to the user."
                )

            else:

                st.success(
                    "The output can pass the output guard."
                )
# =========================================================
# SECURITY POLICY
# =========================================================

elif page == "Security Policy":

    st.title("Security Policy")

    st.write(
        "The application uses risk-based security "
        "decisions to protect the simulated AI agent."
    )

    st.subheader("Risk Thresholds")

    policy_data = {
        "Risk Score": [
            "0–29",
            "30–59",
            "60–79",
            "80–100"
        ],
        "Severity": [
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        ],
        "Action": [
            "ALLOW",
            "BLOCK",
            "BLOCK",
            "BLOCK"
        ]
    }

    import pandas as pd

    policy_df = pd.DataFrame(policy_data)

    st.table(policy_df)

    st.subheader("Security Controls")

    controls = [
        "Input detection",
        "Prompt injection detection",
        "Tool abuse detection",
        "Data exfiltration detection",
        "Risk scoring",
        "Request blocking"
    ]

    for control in controls:
        st.write("✅", control)