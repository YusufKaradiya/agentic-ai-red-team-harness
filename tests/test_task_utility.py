import pandas as pd

from core.evaluator import calculate_task_utility


def test_task_utility():
    df = pd.DataFrame([
        {
            "expected": "ALLOW",
            "actual": "ALLOW"
        },
        {
            "expected": "ALLOW",
            "actual": "BLOCK"
        },
        {
            "expected": "BLOCK",
            "actual": "BLOCK"
        }
    ])

    utility = calculate_task_utility(df)

    assert utility == 50