def generate_ai_alerts(df):

    alerts = []

    for _, row in df.iterrows():

        if row["anomaly"] == -1:

            alerts.append({
                "ip": row["ip"],
                "failed": row["failed"],
                "success": row["success"],
                "risk": "HIGH",
                "reason": "Unusual login behavior detected"
            })

    return alerts