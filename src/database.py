import sqlite3
from datetime import datetime
from geoip import get_location

DB = "security_logs.db"


def init_db():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            ip TEXT,
            alert_type TEXT,
            risk TEXT,
            timestamp TEXT,
            country TEXT,
            city TEXT,
            lat REAL,
            lon REAL
        )
    """)

    conn.commit()
    conn.close()


def save_alert(
    ip,
    alert_type,
    risk
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    location = get_location(ip)

    cursor.execute("""
        INSERT INTO alerts
        (
            ip,
            alert_type,
            risk,
            timestamp,
            country,
            city,
            lat,
            lon
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
    """,
    (
        ip,
        alert_type,
        risk,
        timestamp,
        location["country"],
        location["city"],
        location["lat"],
        location["lon"]
    ))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM alerts
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_stats():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM alerts"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE risk='HIGH'"
    )

    high = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE risk='MEDIUM'"
    )

    medium = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE risk='LOW'"
    )

    low = cursor.fetchone()[0]

    conn.close()

    return (
        total,
        high,
        medium,
        low
    )


def get_top_ips():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ip,
            COUNT(*) as attacks
        FROM alerts
        GROUP BY ip
        ORDER BY attacks DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_attack_locations():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ip,
            country,
            city,
            lat,
            lon,
            alert_type,
            risk,
            timestamp
        FROM alerts
        WHERE lat IS NOT NULL
        AND lon IS NOT NULL
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


if __name__ == "__main__":

    init_db()

    print(
        "Database initialized successfully."
    )