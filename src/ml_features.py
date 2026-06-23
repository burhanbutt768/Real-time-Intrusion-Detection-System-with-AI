from collections import defaultdict


def extract_log_features(logs):

    ip_stats = defaultdict(lambda: {
        "failed": 0,
        "success": 0
    })

    for log in logs:

        if "from" not in log:
            continue

        ip = log.split("from")[-1].strip()

        if "Failed password" in log:
            ip_stats[ip]["failed"] += 1

        elif "Accepted password" in log:
            ip_stats[ip]["success"] += 1

    features = []

    for ip, stats in ip_stats.items():

        features.append([
            ip,
            stats["failed"],
            stats["success"]
        ])

    return features