def plan_tool(user_input):
    text = user_input.lower()

    if "calculate" in text:
        return "Calculator"

    if "multiply" in text:
        return "Calculator"

    if "divide" in text:
        return "Calculator"

    if "add" in text:
        return "Calculator"

    if "subtract" in text:
        return "Calculator"

    if "read" in text and "notes" in text:
        return "File Reader"

    if "product notes" in text:
        return "File Reader"

    if "customer database" in text:
        return "Customer Database"

    if "customer records" in text:
        return "Customer Database"

    if "send email" in text:
        return "Email Sender"

    return None