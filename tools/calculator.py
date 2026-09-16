def calculate(a, b, operation):
    """
    Simple mock calculator tool.
    """

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return "Unsupported operation."