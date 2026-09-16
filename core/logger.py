import sqlite3
import json
from datetime import datetime
from pathlib import Path


DB_PATH = Path("logs/security_events.db")


def initialize_database():
    """
    Create the logs directory and SQLite database if they do not exist.
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id TEXT UNIQUE NOT NULL,
            timestamp TEXT NOT NULL,
            source TEXT,
            attack_id TEXT,
            category TEXT,
            risk_score INTEGER,
            severity TEXT,
            decision TEXT,
            tool TEXT,
            tool_permission TEXT,
            leakage_detected TEXT,
            reasons TEXT,
            action TEXT,
            payload TEXT
        )
        """
    )

    connection.commit()
    connection.close()


def log_security_event(
    source,
    attack_id=None,
    category=None,
    risk_score=0,
    severity=None,
    decision=None,
    tool=None,
    tool_permission=None,
    leakage_detected=False,
    reasons=None,
    action=None,
    payload=None
):
    """
    Save a security event into SQLite.
    """

    initialize_database()

    timestamp = datetime.now().isoformat(timespec="seconds")

    event_id = (
        datetime.now().strftime("%Y%m%d%H%M%S%f")
    )

    if reasons is None:
        reasons = []

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO security_events (
            event_id,
            timestamp,
            source,
            attack_id,
            category,
            risk_score,
            severity,
            decision,
            tool,
            tool_permission,
            leakage_detected,
            reasons,
            action,
            payload
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            event_id,
            timestamp,
            source,
            attack_id,
            category,
            risk_score,
            severity,
            decision,
            tool,
            tool_permission,
            "YES" if leakage_detected else "NO",
            json.dumps(reasons),
            action,
            payload
        )
    )

    connection.commit()
    connection.close()

    return event_id


def get_security_events():
    """
    Retrieve all security events.
    """

    initialize_database()

    connection = sqlite3.connect(DB_PATH)

    query = """
        SELECT
            id,
            event_id,
            timestamp,
            attack_id,
            source,
            category,
            risk_score,
            severity,
            decision,
            tool,
            tool_permission,
            leakage_detected,
            reasons,
            action,
            payload
        FROM security_events
        ORDER BY id DESC
    """

    rows = connection.execute(query).fetchall()

    columns = [
        "id",
        "event_id",
        "timestamp",
        "attack_id",
        "source",
        "category",
        "risk_score",
        "severity",
        "decision",
        "tool",
        "tool_permission",
        "leakage_detected",
        "reasons",
        "action",
        "payload"
    ]

    connection.close()

    return rows, columns


def clear_security_events():
    """
    Delete all security events.
    """

    initialize_database()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM security_events")

    connection.commit()
    connection.close()