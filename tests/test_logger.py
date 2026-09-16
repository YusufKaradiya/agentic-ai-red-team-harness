from core.logger import (
    initialize_database,
    log_security_event,
    get_security_events
)


def test_database_initialization():

    initialize_database()

    rows, columns = get_security_events()

    assert "event_id" in columns
    assert "timestamp" in columns
    assert "decision" in columns


def test_security_event_logging():

    event_id = log_security_event(
        source="Unit Test",
        attack_id="TEST001",
        category="Test Attack",
        risk_score=80,
        severity="CRITICAL",
        decision="BLOCK",
        tool="Test Tool",
        leakage_detected=True,
        reasons=["Synthetic secret detected"],
        action="Request blocked",
        payload="Synthetic test payload"
    )

    assert event_id is not None

    rows, columns = get_security_events()

    assert len(rows) > 0

    latest_event = rows[0]

    assert latest_event[3] == "TEST001"
    assert latest_event[5] == "Test Attack"
    assert latest_event[6] == 80
    assert latest_event[8] == "BLOCK"


def test_logged_leakage_event():

    log_security_event(
        source="Leakage Test",
        category="Data Leakage",
        risk_score=80,
        severity="CRITICAL",
        decision="BLOCK",
        leakage_detected=True,
        reasons=["Synthetic secret detected"]
    )

    rows, columns = get_security_events()

    leakage_values = [
        row[11]
        for row in rows
    ]

    assert "YES" in leakage_values