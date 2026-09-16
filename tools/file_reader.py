def read_file(filename):
    """
    Mock file reader.

    Only reads files from the synthetic documents folder.
    """

    allowed_files = [
        "safe_report.txt",
        "customer_notes.txt",
        "support_ticket.txt",
        "product_notes.txt"
    ]

    if filename not in allowed_files:

        return "File access denied."

    path = f"data/documents/{filename}"

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except FileNotFoundError:

        return "File not found."