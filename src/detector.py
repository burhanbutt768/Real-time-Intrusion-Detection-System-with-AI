#rule base detection

from collections import defaultdict


def detect_bruteforce(logs, threshold=3):

    failed_attempts = defaultdict(int)

    for log in logs:

        if "Failed password" in log:

            ip = log.split("from")[-1].strip()

            failed_attempts[ip] += 1

    alerts = []

    for ip, count in failed_attempts.items():

        if count >= threshold:

            if count >= 10:
                risk = "CRITICAL"

            elif count >= 5:
                risk = "HIGH"

            else:
                risk = "MEDIUM"

            alerts.append({
                "ip": ip,
                "attempts": count,
                "risk": risk
            })

    return alerts


def detect_compromised_account(logs):

    failed_ips = set()

    alerts = []

    for log in logs:

        if "Failed password" in log:

            ip = log.split("from")[-1].strip()
            failed_ips.add(ip)

        elif "Accepted password" in log:

            ip = log.split("from")[-1].strip()

            if ip in failed_ips:

                alerts.append({
                    "ip": ip,
                    "type": "Possible Account Compromise",
                    "risk": "CRITICAL"
                })

    return alerts