import pandas as pd

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