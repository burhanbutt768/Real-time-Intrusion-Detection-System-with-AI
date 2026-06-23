from detector import (
    detect_bruteforce,
    detect_compromised_account
)

from ml_features import (
    extract_log_features
)

from anomaly_detector import (
    detect_anomalies
)

from live_monitor import (
    monitor_logs
)

from soc_dashboard import show_dashboard

from database import (
    save_alert,
    init_db   # ✅ IMPORTANT
)


LOG_FILE = "../logs/auth.log"

last_position = 0


def read_new_logs():

    global last_position

    with open(
        LOG_FILE,
        "r"
    ) as file:

        file.seek(
            last_position
        )

        new_logs = file.readlines()

        last_position = (
            file.tell()
        )

    return new_logs


def analyze():

    logs = read_new_logs()

    if not logs:
        return

    print("\n===== NEW EVENTS =====")

    # Show raw logs
    for log in logs:
        print("\n📄", log.strip())

    # Rule Detection
    alerts = detect_bruteforce(logs)

    for alert in alerts:

        print("\n⚠ BRUTE FORCE")
        print("IP:", alert["ip"])
        print("Attempts:", alert["attempts"])
        print("Risk:", alert["risk"])

        save_alert(
            alert["ip"],
            "Brute Force",
            alert["risk"]
        )

    # Compromise Detection
    compromise = detect_compromised_account(logs)

    for alert in compromise:

        print("\n🚨 ACCOUNT COMPROMISE")
        print("IP:", alert["ip"])
        print("Risk:", alert["risk"])

        save_alert(
            alert["ip"],
            "Compromise",
            alert["risk"]
        )

    # Dashboard
    show_dashboard(
        total=len(logs),
        brute=len(alerts),
        compromise=len(compromise),
        ai=0
    )

    # AI Detection
    features = extract_log_features(logs)

    if features:

        results = detect_anomalies(features)

        print("\n=== AI ANALYSIS ===")

        for _, row in results.iterrows():

            if row["anomaly"] == -1:

                print("\n============")
                print("🤖 AI ALERT")

                print("IP:", row["ip"])
                print("Failed:", row["failed"])
                print("Success:", row["success"])
                print("Risk: HIGH")

                save_alert(
                    row["ip"],
                    "AI Alert",
                    "HIGH"
                )

            else:

                print("\n=============")
                print("✅ NORMAL")
                print("IP:", row["ip"])


# Start from end of file
with open(LOG_FILE, "r") as file:
    file.seek(0, 2)
    last_position = file.tell()


# ✅ VERY IMPORTANT: Initialize DB BEFORE monitoring
init_db()


monitor_logs(
    LOG_FILE,
    analyze
)