import pandas as pd


def validate_data(data):
    print("\n========== DATA VALIDATION ==========")

    # Check missing values
    print("\nMissing values:")
    print(data.isnull().sum())

    # Check duplicate transactions
    duplicates = data.duplicated().sum()
    print(f"\nDuplicate rows: {duplicates}")

    # Check invalid transaction amounts
    invalid_amounts = (data["amount"] <= 0).sum()
    print(f"Invalid transaction amounts: {invalid_amounts}")

    # Convert transaction date to datetime
    data["transaction_date"] = pd.to_datetime(
        data["transaction_date"],
        errors="coerce"
    )

    # Check invalid dates
    invalid_dates = data["transaction_date"].isnull().sum()
    print(f"Invalid transaction dates: {invalid_dates}")

    return data


def clean_data(data):
    print("\n========== DATA CLEANING ==========")

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Remove transactions with invalid amounts
    data = data[data["amount"] > 0]

    # Remove rows with invalid dates
    data = data.dropna(subset=["transaction_date"])

    # Reset index after cleaning
    data = data.reset_index(drop=True)

    print("Data cleaning completed.")
    print(f"Transactions after cleaning: {len(data)}")

    return data