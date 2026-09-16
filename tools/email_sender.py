def send_email(to, subject, message):
    """
    Mock email sender.

    Does NOT send a real email.
    """

    return {
        "status": "SIMULATED",
        "to": to,
        "subject": subject,
        "message": message
    }