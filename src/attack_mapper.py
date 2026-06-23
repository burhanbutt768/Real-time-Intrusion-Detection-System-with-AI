def map_attack(alert):

    if alert["failed"] >= 10:

        return {
            "technique": "Brute Force",
            "id": "T1110",
            "tactic": "Credential Access"
        }

    elif alert["failed"] >= 3:

        return {
            "technique": "Password Guessing",
            "id": "T1110.001",
            "tactic": "Credential Access"
        }

    return {
        "technique": "Suspicious Activity",
        "id": "Unknown",
        "tactic": "Investigation Needed"
    }