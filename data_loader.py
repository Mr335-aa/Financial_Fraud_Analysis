import pandas as pd


def load_transactions(file_path):
    try:
        data = pd.read_csv(file_path)

        print("Transaction data loaded successfully.")
        print(f"Total transactions: {len(data)}")

        return data

    except FileNotFoundError:
        print("Error: Transaction file was not found.")
        return None

    except Exception as e:
        print(f"Error while loading data: {e}")
        return None