def basic_analysis(data):

    print("\n========== BASIC TRANSACTION ANALYSIS ==========")

    total_transactions = len(data)
    total_amount = data["amount"].sum()
    average_amount = data["amount"].mean()
    highest_amount = data["amount"].max()
    lowest_amount = data["amount"].min()

    print(f"Total transactions : {total_transactions}")
    print(f"Total transaction amount : ₹{total_amount:.2f}")
    print(f"Average transaction amount : ₹{average_amount:.2f}")
    print(f"Highest transaction : ₹{highest_amount:.2f}")
    print(f"Lowest transaction : ₹{lowest_amount:.2f}")

    return {
        "total_transactions": total_transactions,
        "total_amount": total_amount,
        "average_amount": average_amount,
        "highest_amount": highest_amount,
        "lowest_amount": lowest_amount
    }


def fraud_analysis(data):

    print("\n========== FRAUD ANALYTICS ==========")

    suspicious_transactions = data[data["fraud_score"] > 0]

    suspicious_count = len(suspicious_transactions)

    total_transactions = len(data)

    fraud_percentage = (
        suspicious_count / total_transactions
    ) * 100

    print(f"Suspicious transactions : {suspicious_count}")
    print(f"Fraud risk percentage : {fraud_percentage:.2f}%")

    print("\nRisk Level Summary:")
    print(data["risk_level"].value_counts())

    print("\nFraud by Transaction Type:")
    print(
        data[data["fraud_score"] > 0]["transaction_type"]
        .value_counts()
    )

    print("\nFraud by Location:")
    print(
        data[data["fraud_score"] > 0]["location"]
        .value_counts()
    )

    return {
        "suspicious_count": suspicious_count,
        "fraud_percentage": fraud_percentage
    }