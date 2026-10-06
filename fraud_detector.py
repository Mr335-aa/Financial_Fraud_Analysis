def detect_fraud(data):

    print("\n========== FRAUD DETECTION ==========")

    data["fraud_score"] = 0
    data["fraud_reason"] = ""

    for index, row in data.iterrows():

        score = 0
        reasons = []

        # Rule 1: Very high transaction amount
        if row["amount"] >= 50000:
            score += 50
            reasons.append("Very high transaction amount")

        # Rule 2: Large transfer
        if row["transaction_type"] == "Transfer" and row["amount"] >= 30000:
            score += 30
            reasons.append("Large transfer")

        # Rule 3: Bank transfer with high amount
        if row["payment_method"] == "Bank Transfer" and row["amount"] >= 40000:
            score += 20
            reasons.append("High-value bank transfer")

        data.at[index, "fraud_score"] = min(score, 100)
        data.at[index, "fraud_reason"] = ", ".join(reasons)

    return data


def assign_risk_level(data):

    def risk_level(score):

        if score >= 70:
            return "HIGH"

        elif score >= 30:
            return "MEDIUM"

        else:
            return "LOW"

    data["risk_level"] = data["fraud_score"].apply(risk_level)

    return data