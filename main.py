from data_loader import load_transactions
from validator import validate_data, clean_data
from analyzer import basic_analysis, fraud_analysis
from fraud_detector import detect_fraud, assign_risk_level
from visualizer import (
    fraud_distribution_chart,
    transaction_amount_chart,
    fraud_location_chart
)


def main():

    file_path = "data/transactions.csv"

    try:

        # Load data
        transactions = load_transactions(file_path)

        if transactions is None:
            print("Unable to load transaction data.")
            return

        # Validate data
        transactions = validate_data(transactions)

        # Clean data
        transactions = clean_data(transactions)

        # Basic analysis
        basic_analysis(transactions)

        # Fraud detection
        transactions = detect_fraud(transactions)

        # Assign risk level
        transactions = assign_risk_level(transactions)

        # Fraud analytics
        fraud_analysis(transactions)

        # Display suspicious transactions
        print("\n========== SUSPICIOUS TRANSACTIONS ==========")

        suspicious = transactions[
            transactions["fraud_score"] > 0
        ]

        if len(suspicious) > 0:

            print(
                suspicious[
                    [
                        "transaction_id",
                        "customer_id",
                        "amount",
                        "transaction_type",
                        "location",
                        "fraud_score",
                        "risk_level",
                        "fraud_reason"
                    ]
                ].to_string(index=False)
            )

        else:
            print("No suspicious transactions detected.")

        # Display charts
        fraud_distribution_chart(transactions)
        transaction_amount_chart(transactions)
        fraud_location_chart(transactions)

    except Exception as e:

        print("\nAn unexpected error occurred.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    main()