import matplotlib.pyplot as plt


def fraud_distribution_chart(data):

    risk_counts = data["risk_level"].value_counts()

    plt.figure(figsize=(7, 5))

    risk_counts.plot(kind="bar")

    plt.title("Transaction Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Transactions")

    plt.tight_layout()
    plt.show()


def transaction_amount_chart(data):

    plt.figure(figsize=(8, 5))

    plt.hist(data["amount"], bins=10)

    plt.title("Transaction Amount Distribution")
    plt.xlabel("Transaction Amount")
    plt.ylabel("Number of Transactions")

    plt.tight_layout()
    plt.show()


def fraud_location_chart(data):

    fraud_data = data[data["fraud_score"] > 0]

    location_counts = fraud_data["location"].value_counts()

    plt.figure(figsize=(8, 5))

    location_counts.plot(kind="bar")

    plt.title("Suspicious Transactions by Location")
    plt.xlabel("Location")
    plt.ylabel("Suspicious Transactions")

    plt.tight_layout()
    plt.show()