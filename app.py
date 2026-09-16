import pandas as pd
import streamlit as st
from core.defense import apply_defense
from core.detector import detect_indirect_injection
from core.leakage_guard import detect_sensitive_data
from core.logger import (
    clear_security_events,
    get_security_events,
    log_security_event,
)
from core.permissions import check_tool_permission

st.set_page_config(
    page_title="Agentic AI Red-Team Harness", page_icon="🛡️", layout="wide"
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
        "Audit Logs",
        "Security Policy",
    ],
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
        st.metric("Total Attacks", len(attacks))

    with col2:
        st.metric(
            "Direct Injection",
            len(
                attacks[
                    attacks["category"] == "Direct Prompt Injection"
                ]
            ),
        )

    with col3:
        st.metric(
            "Tool Abuse",
            len(attacks[attacks["category"] == "Tool Abuse"]),
        )

    with col4:
        st.metric(
            "Data Exfiltration",
            len(
                attacks[
                    attacks["category"] == "Data Exfiltration"
                ]
            ),
        )

    st.divider()

    st.subheader("Attack Corpus")

    st.dataframe(attacks, use_container_width=True)


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
        "Select Attack Category", categories
    )

    # Filter attacks
    filtered_attacks = attacks[
        attacks["category"] == selected_category
    ]

    # Attack selection
    selected_id = st.selectbox(
        "Select Attack", filtered_attacks["id"].tolist()
    )

    attack = filtered_attacks[
        filtered_attacks["id"] == selected_id
    ].iloc[0]

    st.subheader("Attack Details")

    st.write("**Attack ID:**", attack["id"])
    st.write("**Category:**", attack["category"])
    st.write("**Severity:**", attack["severity"])
    st.write("**Target Tool:**", attack["tool"])

    st.text_area("Attack Payload", attack["payload"], height=120)

    st.divider()

    result = None

    if st.button("Run Attack"):
        result = apply_defense(attack["payload"])
        log_security_event(
            source="Attack Simulator",
            attack_id=attack["id"],
            category=result["category"],
            risk_score=result["risk_score"],
            severity=result["severity"],
            decision=result["decision"],
            tool=attack["tool"],
            leakage_detected=False,
            reasons=result["reasons"],
            action=result["action"],
            payload=attack["payload"],
        )

    if result is not None:
        st.subheader("Security Decision")

        if result["decision"] == "BLOCK":
            st.error("🚨 REQUEST BLOCKED")
        else:
            st.success("✅ REQUEST ALLOWED")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", result["risk_score"])

        with col2:
            st.metric("Severity", result["severity"])

        with col3:
            st.metric("Decision", result["decision"])

        st.write("### Category")
        st.write(result["category"])

        st.write("### Security Action")
        st.info(result["action"])

        st.write("### Reasons")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.warning(reason)
        else:
            st.success("No suspicious behavior detected.")


# =========================
# INDIRECT INJECTION
# =========================

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
        "product_notes.txt",
    ]

    selected_document = st.selectbox(
        "Select Document", documents
    )

    document_path = f"{document_folder}/{selected_document}"

    with open(document_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    st.subheader("Document Content")

    st.code(document_text, language="text")

    st.divider()

    if st.button("🔍 Scan Document", use_container_width=True):
        result = detect_indirect_injection(document_text)

        log_security_event(
            source="Indirect Injection Scanner",
            attack_id=selected_document,
            category=result["category"],
            risk_score=result["risk_score"],
            severity=result["severity"],
            decision=result["decision"],
            tool="File Reader",
            leakage_detected=False,
            reasons=result["reasons"],
            action=(
                "Document blocked"
                if result["decision"] == "BLOCK"
                else "Document allowed"
            ),
            payload=document_text,
        )

        st.subheader("Security Result")

        if result["decision"] == "BLOCK":
            st.error("🚨 MALICIOUS DOCUMENT CONTENT DETECTED")
        else:
            st.success("✅ DOCUMENT CONTENT APPEARS SAFE")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", result["risk_score"])

        with col2:
            st.metric("Severity", result["severity"])

        with col3:
            st.metric("Decision", result["decision"])

        st.divider()

        st.subheader("Detected Category")
        st.info(result["category"])

        st.subheader("Detection Reasons")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.warning(f"⚠️ {reason}")
        else:
            st.success("No suspicious instructions detected.")

        st.divider()

        st.subheader("Security Interpretation")

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


# =========================
# TOOL SANDBOX
# =========================

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
        "Email Sender",
    ]

    selected_tool = st.selectbox("Select Tool", tools)

    st.divider()

    st.subheader("Permission Check")

    permission = check_tool_permission(selected_tool)
    log_security_event(
        source="Tool Sandbox",
        category="Tool Authorization",
        risk_score=0 if permission["allowed"] else 70,
        severity="LOW" if permission["allowed"] else "HIGH",
        decision="ALLOW" if permission["allowed"] else "BLOCK",
        tool=selected_tool,
        tool_permission="ALLOW" if permission["allowed"] else "BLOCK",
        leakage_detected=False,
        reasons=[permission["reason"]],
        action=(
            "Tool authorized"
            if permission["allowed"]
            else "Tool access blocked"
        )
    )
    if permission["allowed"]:
        st.success("✅ TOOL AUTHORIZED")
    else:
        st.error("🚨 TOOL ACCESS BLOCKED")

    st.write(f"**Tool:** {selected_tool}")
    st.write(f"**Reason:** {permission['reason']}")

    st.divider()

    st.subheader("Tool Permission Matrix")

    permission_data = []

    for tool in tools:
        result = check_tool_permission(tool)
        permission_data.append(
            {
                "Tool": tool,
                "Permission": "ALLOW" if result["allowed"] else "BLOCK",
                "Reason": result["reason"],
            }
        )

    permission_df = pd.DataFrame(permission_data)

    st.dataframe(
        permission_df, use_container_width=True, hide_index=True
    )


# =========================
# OUTPUT GUARD
# =========================

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
            "Example: The API key is SYNTHETIC_API_KEY_12345"
        ),
    )

    if st.button("🔍 Scan Output", use_container_width=True):
        if not output_text.strip():
            st.warning("Please enter some output to scan.")
        else:
            result = detect_sensitive_data(output_text)
            log_security_event(
                source="Output Guard",
                category="Data Leakage",
                risk_score=result["risk_score"],
                severity="CRITICAL" if result["leak_detected"] else "LOW",
                decision=result["decision"],
                leakage_detected=result["leak_detected"],
                reasons=result["findings"],
                action=(
                    "Output blocked"
                    if result["leak_detected"]
                    else "Output allowed"
                ),
                payload=output_text,
            )
            st.divider()

            st.subheader("Security Result")

            if result["leak_detected"]:
                st.error("🚨 SENSITIVE DATA LEAK DETECTED")
            else:
                st.success("✅ NO SENSITIVE DATA DETECTED")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Leak Detected",
                    "YES" if result["leak_detected"] else "NO",
                )

            with col2:
                st.metric("Risk Score", result["risk_score"])

            with col3:
                st.metric("Decision", result["decision"])

            st.divider()

            st.subheader("Detection Findings")

            if result["findings"]:
                for finding in result["findings"]:
                    st.warning(f"⚠️ {finding}")
            else:
                st.success("No sensitive information was found.")

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
elif page == "Audit Logs":

    st.title("📋 Security Audit Logs")

    st.write(
        "This module records security events generated by the "
        "red-team harness."
    )

    st.divider()

    rows, columns = get_security_events()

    if not rows:
        st.info(
            "No security events have been recorded yet. "
            "Run an attack or security test first."
        )

    else:

        logs_df = pd.DataFrame(rows, columns=columns)

        total_events = len(logs_df)

        blocked_events = len(
            logs_df[logs_df["decision"] == "BLOCK"]
        )

        allowed_events = len(
            logs_df[logs_df["decision"] == "ALLOW"]
        )

        leakage_events = len(
            logs_df[logs_df["leakage_detected"] == "YES"]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Events",
                total_events
            )

        with col2:
            st.metric(
                "Blocked",
                blocked_events
            )

        with col3:
            st.metric(
                "Allowed",
                allowed_events
            )

        with col4:
            st.metric(
                "Leakage Events",
                leakage_events
            )

        st.divider()

        st.subheader("🔎 Filters")

        col1, col2, col3 = st.columns(3)

        with col1:
            source_options = [
                "All"
            ] + sorted(
                logs_df["source"].dropna().unique().tolist()
            )

            selected_source = st.selectbox(
                "Source",
                source_options
            )

        with col2:
            decision_options = [
                "All",
                "ALLOW",
                "BLOCK"
            ]

            selected_decision = st.selectbox(
                "Decision",
                decision_options
            )

        with col3:
            severity_options = [
                "All"
            ] + sorted(
                logs_df["severity"].dropna().unique().tolist()
            )

            selected_severity = st.selectbox(
                "Severity",
                severity_options
            )

        filtered_df = logs_df.copy()

        if selected_source != "All":
            filtered_df = filtered_df[
                filtered_df["source"] == selected_source
            ]

        if selected_decision != "All":
            filtered_df = filtered_df[
                filtered_df["decision"] == selected_decision
            ]

        if selected_severity != "All":
            filtered_df = filtered_df[
                filtered_df["severity"] == selected_severity
            ]

        st.divider()

        st.subheader("📊 Security Events")

        display_columns = [
            "event_id",
            "timestamp",
            "source",
            "attack_id",
            "category",
            "risk_score",
            "severity",
            "decision",
            "tool",
            "tool_permission",
            "leakage_detected"
        ]

        st.dataframe(
            filtered_df[display_columns],
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("🔍 Event Details")

        selected_event = st.selectbox(
            "Select Event ID",
            filtered_df["event_id"].tolist()
        )

        event = filtered_df[
            filtered_df["event_id"] == selected_event
        ].iloc[0]

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Event ID:**")
            st.write(event["event_id"])

            st.write("**Timestamp:**")
            st.write(event["timestamp"])

            st.write("**Source:**")
            st.write(event["source"])

            st.write("**Attack ID:**")
            st.write(event["attack_id"])

            st.write("**Category:**")
            st.write(event["category"])

        with col2:

            st.write("**Risk Score:**")
            st.write(event["risk_score"])

            st.write("**Severity:**")
            st.write(event["severity"])

            st.write("**Decision:**")
            st.write(event["decision"])

            st.write("**Tool:**")
            st.write(event["tool"])

            st.write("**Tool Permission:**")
            st.write(event["tool_permission"])

            st.write("**Leakage Detected:**")
            st.write(event["leakage_detected"])

        st.divider()

        st.subheader("Detection Reasons")
        st.write(event["reasons"])

        st.subheader("Security Action")
        st.write(event["action"])

        st.subheader("Recorded Payload")
        st.code(
            str(event["payload"]),
            language="text"
        )

        st.divider()

        if st.button(
            "🗑️ Clear All Audit Logs",
            use_container_width=True
        ):

            clear_security_events()

            st.success(
                "All audit logs have been cleared."
            )

            st.rerun()

# =========================
# SECURITY POLICY
# =========================

elif page == "Security Policy":
    st.title("Security Policy")

    st.write(
        "The application uses risk-based security "
        "decisions to protect the simulated AI agent."
    )

    st.subheader("Risk Thresholds")

    policy_data = {
        "Risk Score": ["0–29", "30–59", "60–79", "80–100"],
        "Severity": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        "Action": ["ALLOW", "BLOCK", "BLOCK", "BLOCK"],
    }

    policy_df = pd.DataFrame(policy_data)

    st.table(policy_df)

    st.subheader("Security Controls")

    controls = [
        "Input detection",
        "Prompt injection detection",
        "Tool abuse detection",
        "Data exfiltration detection",
        "Risk scoring",
        "Request blocking",
    ]

    for control in controls:
        st.write("✅", control)