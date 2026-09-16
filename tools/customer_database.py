# Synthetic customer records only.
# No real customer information is used.


CUSTOMERS = [
    {
        "id": "C001",
        "name": "Synthetic Customer 1",
        "email": "customer1@example.test",
        "status": "Active"
    },
    {
        "id": "C002",
        "name": "Synthetic Customer 2",
        "email": "customer2@example.test",
        "status": "Active"
    },
    {
        "id": "C003",
        "name": "Synthetic Customer 3",
        "email": "customer3@example.test",
        "status": "Inactive"
    }
]


def get_customers():
    """
    Return synthetic customer records.
    """

    return CUSTOMERS