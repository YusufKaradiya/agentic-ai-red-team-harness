def generate_mutations(payload):
    """
    Generate simple adversarial variations of a payload.

    These mutations are deterministic and designed for
    reproducible security testing.
    """

    mutations = []

    # -------------------------
    # Original
    # -------------------------

    mutations.append({
        "mutation_type": "Original",
        "payload": payload
    })

    # -------------------------
    # Case variation
    # -------------------------

    mutations.append({
        "mutation_type": "Uppercase",
        "payload": payload.upper()
    })

    mutations.append({
        "mutation_type": "Lowercase",
        "payload": payload.lower()
    })

    # -------------------------
    # Whitespace variation
    # -------------------------

    mutations.append({
        "mutation_type": "Extra Whitespace",
        "payload": payload.replace(
            " ",
            "   "
        )
    })

    # -------------------------
    # Newline variation
    # -------------------------

    mutations.append({
        "mutation_type": "Newline Injection",
        "payload": payload.replace(
            " ",
            "\n"
        )
    })

    return mutations
import pandas as pd

from core.defense import apply_defense


def evaluate_mutations(mutations_df):
    """
    Evaluate unseen/mutated attacks against the current
    defense engine.
    """

    results = []

    for _, row in mutations_df.iterrows():

        result = apply_defense(
            row["payload"]
        )

        expected = row[
            "expected_action"
        ].upper()

        actual = result[
            "decision"
        ]

        if (
            expected == "BLOCK"
            and actual == "BLOCK"
        ):
            result_type = "Detected"

        elif (
            expected == "BLOCK"
            and actual == "ALLOW"
        ):
            result_type = "Bypass"

        elif (
            expected == "ALLOW"
            and actual == "BLOCK"
        ):
            result_type = "False Positive"

        else:
            result_type = "Correct Allow"

        results.append({
            "id": row["id"],
            "base_category":
                row["base_category"],
            "mutation_type":
                row["mutation_type"],
            "payload":
                row["payload"],
            "expected":
                expected,
            "actual":
                actual,
            "risk_score":
                result["risk_score"],
            "severity":
                result["severity"],
            "result":
                result_type,
            "reasons":
                result["reasons"]
        })

    return pd.DataFrame(results)
def calculate_residual_risk(results_df):
    """
    Calculate residual risk from attacks that bypass
    the current defense.
    """

    malicious = results_df[
        results_df["expected"] == "BLOCK"
    ]

    total_attacks = len(malicious)

    bypasses = malicious[
        malicious["result"] == "Bypass"
    ]

    bypass_count = len(bypasses)

    if total_attacks > 0:

        bypass_rate = (
            bypass_count
            /
            total_attacks
        ) * 100

    else:

        bypass_rate = 0

    return {
        "total_attacks": total_attacks,
        "bypasses": bypass_count,
        "bypass_rate": bypass_rate
    }