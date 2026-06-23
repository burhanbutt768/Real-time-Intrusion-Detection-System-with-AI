from log_parser import read_logs
from detector import detect_bruteforce, detect_compromised_account
from report_generator import generate_report
from ml_features import extract_log_features
from anomaly_detector import detect_anomalies, train_model
from ai_alerts import generate_ai_alerts
from attack_mapper import map_attack
from database import init_db



init_db()

logs = read_logs("../logs/auth.log")

# Brute Force Detection
bruteforce_alerts = detect_bruteforce(logs)

for alert in bruteforce_alerts:

    print("\n⚠ BRUTE FORCE ALERT")
    print("IP:", alert["ip"])
    print("Attempts:", alert["attempts"])
    print("Risk:", alert["risk"])


# Compromised Account Detection
compromise_alerts = detect_compromised_account(logs)

for alert in compromise_alerts:

    print("\n🚨 SECURITY INCIDENT")
    print("Type:", alert["type"])
    print("IP:", alert["ip"])
    print("Risk:", alert["risk"])


generate_report(
    bruteforce_alerts,
    compromise_alerts
)

print("\nSecurity report generated successfully.")



#detect anomalies
features = extract_log_features(logs)

# anomaly_results = detect_anomalies(features)
train_model(
    features
)

anomaly_results = detect_anomalies(
    features
)

print("\n=== AI ANOMALY DETECTION ===")
print(anomaly_results)



#generate alerts
ai_alerts = generate_ai_alerts(
    anomaly_results
)

# for alert in ai_alerts:

#     print("\n🤖 AI SECURITY ALERT")

#     print("IP:", alert["ip"])

#     print(
#         "Failed Logins:",
#         alert["failed"]
#     )

#     print(
#         "Successful Logins:",
#         alert["success"]
#     )

#     print(
#         "Risk:",
#         alert["risk"]
#     )

#     print(
#         "Reason:",
#         alert["reason"]
#     )


#Ai alerts with mapping
for alert in ai_alerts:

    attack = map_attack(alert)

    print("\n🤖 AI SECURITY ALERT")

    print("IP:", alert["ip"])

    print(
        "Failed Logins:",
        alert["failed"]
    )

    print(
        "Successful Logins:",
        alert["success"]
    )

    print(
        "Risk:",
        alert["risk"]
    )

    print(
        "Reason:",
        alert["reason"]
    )

    print(
        "Technique:",
        attack["technique"]
    )

    print(
        "ATT&CK ID:",
        attack["id"]
    )

    print(
        "Tactic:",
        attack["tactic"]
    )