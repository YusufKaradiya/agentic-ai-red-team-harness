import pandas as pd
import time
from core.defense import apply_defense
def evaluate_attack_corpus(attacks_df):
    """
    Run the actual detector/defense engine against
    every case in the attack corpus.
    """

    results = []

    for _, attack in attacks_df.iterrows():

        detection = apply_defense(
            attack["payload"]
        )

        expected = attack["expected_action"].upper()
        actual = detection["decision"]

        correct = expected == actual

        if expected == "BLOCK" and actual == "BLOCK":
            result_type = "True Positive"

        elif expected == "ALLOW" and actual == "ALLOW":
            result_type = "True Negative"

        elif expected == "ALLOW" and actual == "BLOCK":
            result_type = "False Positive"

        elif expected == "BLOCK" and actual == "ALLOW":
            result_type = "False Negative"

        else:
            result_type = "Unknown"

        results.append({
            "id": attack["id"],
            "category": attack["category"],
            "severity_expected": attack["severity"],
            "tool": attack["tool"],
            "expected": expected,
            "actual": actual,
            "risk_score": detection["risk_score"],
            "severity_detected": detection["severity"],
            "correct": correct,
            "result_type": result_type
        })

    return pd.DataFrame(results)


def calculate_metrics(results_df):
    """
    Calculate security evaluation metrics.
    """

    total = len(results_df)

    if total == 0:
        return {
            "total_cases": 0,
            "attack_cases": 0,
            "benign_cases": 0,
            "correct": 0,
            "false_positives": 0,
            "false_negatives": 0,
            "detection_rate": 0,
            "attack_success_rate": 0,
            "average_risk_score": 0
        }

    attack_cases = len(
        results_df[
            results_df["expected"] == "BLOCK"
        ]
    )

    benign_cases = len(
        results_df[
            results_df["expected"] == "ALLOW"
        ]
    )

    correct = len(
        results_df[
            results_df["correct"] == True
        ]
    )

    false_positives = len(
        results_df[
            results_df["result_type"] == "False Positive"
        ]
    )

    false_negatives = len(
        results_df[
            results_df["result_type"] == "False Negative"
        ]
    )

    if attack_cases > 0:

        detected_attacks = len(
            results_df[
                (results_df["expected"] == "BLOCK")
                &
                (results_df["actual"] == "BLOCK")
            ]
        )

        detection_rate = (
            detected_attacks / attack_cases
        ) * 100

        successful_attacks = len(
            results_df[
                (results_df["expected"] == "BLOCK")
                &
                (results_df["actual"] == "ALLOW")
            ]
        )

        attack_success_rate = (
            successful_attacks / attack_cases
        ) * 100

    else:

        detection_rate = 0
        attack_success_rate = 0

    average_risk_score = (
        results_df["risk_score"].mean()
    )

    return {
        "total_cases": total,
        "attack_cases": attack_cases,
        "benign_cases": benign_cases,
        "correct": correct,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "detection_rate": detection_rate,
        "attack_success_rate": attack_success_rate,
        "average_risk_score": average_risk_score
    }
def run_proposed(payload):
    """
    Run the proposed layered security system.
    """

    start_time = time.perf_counter()

    result = apply_defense(payload)

    end_time = time.perf_counter()

    latency_ms = (
        end_time - start_time
    ) * 1000

    return {
        "decision": result["decision"],
        "risk_score": result["risk_score"],
        "severity": result["severity"],
        "latency_ms": latency_ms,
        "reasons": result["reasons"]
    }
def compare_baseline_proposed(attacks_df):
    """
    Run the same attack corpus through both systems.
    """

    from core.baseline import run_baseline

    results = []

    for _, attack in attacks_df.iterrows():

        payload = attack["payload"]
        tool = attack["tool"]

        # -------------------------
        # Baseline
        # -------------------------

        baseline = run_baseline(
            payload,
            tool
        )

        # -------------------------
        # Proposed
        # -------------------------

        proposed = run_proposed(
            payload
        )

        expected = attack[
            "expected_action"
        ].upper()

        baseline_actual = baseline[
            "decision"
        ]

        proposed_actual = proposed[
            "decision"
        ]

        # -------------------------
        # Baseline classification
        # -------------------------

        if expected == "BLOCK" and baseline_actual == "BLOCK":
            baseline_result = "True Positive"

        elif expected == "ALLOW" and baseline_actual == "ALLOW":
            baseline_result = "True Negative"

        elif expected == "ALLOW" and baseline_actual == "BLOCK":
            baseline_result = "False Positive"

        else:
            baseline_result = "False Negative"

        # -------------------------
        # Proposed classification
        # -------------------------

        if expected == "BLOCK" and proposed_actual == "BLOCK":
            proposed_result = "True Positive"

        elif expected == "ALLOW" and proposed_actual == "ALLOW":
            proposed_result = "True Negative"

        elif expected == "ALLOW" and proposed_actual == "BLOCK":
            proposed_result = "False Positive"

        else:
            proposed_result = "False Negative"

        results.append({
            "id": attack["id"],
            "category": attack["category"],
            "expected": expected,

            "baseline_decision":
                baseline_actual,

            "baseline_result":
                baseline_result,

            "baseline_tool_executed":
                baseline["tool_executed"],

            "baseline_latency_ms":
                baseline["latency_ms"],

            "proposed_decision":
                proposed_actual,

            "proposed_result":
                proposed_result,

            "proposed_risk_score":
                proposed["risk_score"],

            "proposed_latency_ms":
                proposed["latency_ms"]
        })

    return pd.DataFrame(results)
def calculate_system_metrics(
    results_df,
    system_prefix
):
    """
    Calculate metrics for either baseline or proposed system.
    """

    decision_column = (
        f"{system_prefix}_decision"
    )

    result_column = (
        f"{system_prefix}_result"
    )

    total = len(results_df)

    attacks = len(
        results_df[
            results_df["expected"] == "BLOCK"
        ]
    )

    benign = len(
        results_df[
            results_df["expected"] == "ALLOW"
        ]
    )

    true_positives = len(
        results_df[
            results_df[result_column]
            == "True Positive"
        ]
    )

    true_negatives = len(
        results_df[
            results_df[result_column]
            == "True Negative"
        ]
    )

    false_positives = len(
        results_df[
            results_df[result_column]
            == "False Positive"
        ]
    )

    false_negatives = len(
        results_df[
            results_df[result_column]
            == "False Negative"
        ]
    )

    correct = (
        true_positives
        +
        true_negatives
    )

    detection_rate = (
        true_positives / attacks * 100
        if attacks > 0
        else 0
    )

    attack_success_rate = (
        false_negatives / attacks * 100
        if attacks > 0
        else 0
    )

    false_positive_rate = (
        false_positives / benign * 100
        if benign > 0
        else 0
    )

    accuracy = (
        correct / total * 100
        if total > 0
        else 0
    )

    latency_column = (
        f"{system_prefix}_latency_ms"
    )

    average_latency = (
        results_df[latency_column].mean()
        if latency_column in results_df.columns
        else 0
    )

    return {
        "total": total,
        "attacks": attacks,
        "benign": benign,
        "true_positives": true_positives,
        "true_negatives": true_negatives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "detection_rate": detection_rate,
        "attack_success_rate": attack_success_rate,
        "false_positive_rate": false_positive_rate,
        "accuracy": accuracy,
        "average_latency_ms": average_latency
    }