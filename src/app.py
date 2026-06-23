import streamlit as st
import pandas as pd
import plotly.express as px
import folium

from streamlit_autorefresh import st_autorefresh
from streamlit_folium import st_folium

from database import (
    get_history,
    get_stats,
    get_top_ips,
    get_attack_locations
)

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Security Operations Center",
    page_icon="🛡",
    layout="wide"
)

# ------------------------------------
# AUTO REFRESH
# ------------------------------------

st_autorefresh(
    interval=5000,
    key="soc_refresh"
)

# ------------------------------------
# LOAD DATA
# ------------------------------------

history = get_history()

df = pd.DataFrame(
    history,
    columns=[
        "ID",
        "IP",
        "Attack Type",
        "Risk",
        "Timestamp",
        "Country",
        "City",
        "Lat",
        "Lon"
    ]
)

total, high, medium, low = get_stats()

# ------------------------------------
# HEADER
# ------------------------------------

st.title("🛡 Security Operations Center")

st.caption(
    "Real-Time AI-Powered Intrusion Detection Dashboard"
)

# ------------------------------------
# METRICS
# ------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Alerts",
    total
)

c2.metric(
    "High Risk",
    high
)

c3.metric(
    "Medium Risk",
    medium
)

c4.metric(
    "Low Risk",
    low
)

st.divider()

# ------------------------------------
# ATTACK DISTRIBUTION + RISK BREAKDOWN
# ------------------------------------

left, right = st.columns(2)

with left:

    st.subheader(
        "📊 Attack Distribution"
    )

    if not df.empty:

        attack_counts = (
            df["Attack Type"]
            .value_counts()
            .reset_index()
        )

        attack_counts.columns = [
            "Attack Type",
            "Count"
        ]

        fig = px.bar(
            attack_counts,
            x="Attack Type",
            y="Count",
            title="Attack Types"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No alerts available"
        )

with right:

    st.subheader(
        "⚠ Risk Breakdown"
    )

    if not df.empty:

        risk_counts = (
            df["Risk"]
            .value_counts()
            .reset_index()
        )

        risk_counts.columns = [
            "Risk",
            "Count"
        ]

        fig = px.pie(
            risk_counts,
            values="Count",
            names="Risk",
            title="Risk Levels"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No alerts available"
        )

# ------------------------------------
# ATTACK TIMELINE
# ------------------------------------

st.divider()

st.subheader(
    "📈 Attack Timeline"
)

if not df.empty:

    timeline = (
        df.groupby("Timestamp")
        .size()
        .reset_index(name="Count")
    )

    fig = px.line(
        timeline,
        x="Timestamp",
        y="Count",
        markers=True,
        title="Attack Activity Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "No timeline data available"
    )

# ------------------------------------
# TOP ATTACKING IPS
# ------------------------------------

st.divider()

st.subheader(
    "🌐 Top Attacking IP Addresses"
)

if not df.empty:

    ip_counts = (
        df["IP"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    ip_counts.columns = [
        "IP Address",
        "Count"
    ]

    fig = px.bar(
        ip_counts,
        x="IP Address",
        y="Count",
        title="Top Attack Sources"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "No IP data available"
    )

# ------------------------------------
# LIVE ALERT FEED
# ------------------------------------

st.divider()

st.subheader(
    "🚨 Live Alert Feed"
)

if not df.empty:

    live_feed = (
        df.sort_values(
            by="ID",
            ascending=False
        )
        .head(15)
    )

    for _, row in live_feed.iterrows():

        message = (
            f"[{row['Timestamp']}] "
            f"{row['Attack Type']} "
            f"from {row['IP']} "
            f"({row['Country']})"
        )

        if row["Risk"] == "HIGH":

            st.error(message)

        elif row["Risk"] == "MEDIUM":

            st.warning(message)

        else:

            st.info(message)

else:

    st.info(
        "No alerts received"
    )

# ------------------------------------
# LATEST ALERTS
# ------------------------------------

st.divider()

st.subheader(
    "📋 Latest Alerts"
)

if not df.empty:

    latest = (
        df.sort_values(
            by="ID",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        latest[
            [
                "IP",
                "Country",
                "City",
                "Attack Type",
                "Risk",
                "Timestamp"
            ]
        ],
        use_container_width=True
    )

else:

    st.info(
        "No alerts available"
    )

# ------------------------------------
# FULL ATTACK HISTORY
# ------------------------------------

st.divider()

st.subheader(
    "📚 Complete Attack History"
)

if not df.empty:

    st.dataframe(
        df[
            [
                "IP",
                "Country",
                "City",
                "Attack Type",
                "Risk",
                "Timestamp"
            ]
        ].sort_values(
            by="Timestamp",
            ascending=False
        ),
        use_container_width=True,
        height=400
    )

else:

    st.info(
        "Database is empty"
    )

# ------------------------------------
# GLOBAL ATTACK MAP
# ------------------------------------

st.divider()

st.subheader(
    "🌍 Global Attack Map"
)

if not df.empty:

    attack_map = folium.Map(
        location=[20, 0],
        zoom_start=2
    )

    for _, row in df.iterrows():

        if (
            pd.notna(row["Lat"])
            and
            pd.notna(row["Lon"])
        ):

            popup_text = f"""
            <b>IP:</b> {row['IP']}<br>
            <b>Country:</b> {row['Country']}<br>
            <b>City:</b> {row['City']}<br>
            <b>Attack:</b> {row['Attack Type']}<br>
            <b>Risk:</b> {row['Risk']}<br>
            <b>Time:</b> {row['Timestamp']}
            """

            folium.Marker(
                [row["Lat"], row["Lon"]],
                popup=popup_text
            ).add_to(
                attack_map
            )

    st_folium(
        attack_map,
        width=1200,
        height=500
    )

else:

    st.info(
        "No attack locations available."
    )

# ------------------------------------
# FOOTER STATS
# ------------------------------------

st.divider()

if not df.empty:

    unique_ips = (
        df["IP"]
        .nunique()
    )

    unique_countries = (
        df["Country"]
        .nunique()
    )

    st.success(
        f"""
        Unique IPs Detected: {unique_ips}
        | Countries Detected: {unique_countries}
        """
    )

else:

    st.info(
        "No IP addresses detected yet"
    )