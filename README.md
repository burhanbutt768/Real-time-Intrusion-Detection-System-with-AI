# Real-Time Intrusion Detection System

## Overview

The Real-Time Intrusion Detection System (IDS) is a cybersecurity monitoring platform developed using Python, Streamlit, SQLite, Plotly, and Folium.

The system is designed to detect suspicious activities, classify threats based on risk level, store security alerts, and provide real-time visualization through an interactive Security Operations Center (SOC) dashboard.

In addition to attack monitoring, the system performs GeoIP analysis to identify the geographical origin of attackers and displays attack locations on an interactive world map.

---

## Objectives

The primary objective of this project is to:

* Detect and monitor suspicious network activities
* Store attack records in a database
* Classify threats based on severity
* Visualize attack trends and statistics
* Track attacker locations using GeoIP technology
* Provide real-time security monitoring through a dashboard

---

## Features

### 1. Alert Management

The system records all detected attacks and stores them in an SQLite database.

Each alert contains:

* IP Address
* Attack Type
* Risk Level
* Timestamp
* Country
* City
* Latitude
* Longitude

---

### 2. Risk Classification

Detected attacks are classified into:

#### HIGH Risk

Examples:

* Brute Force Attacks
* Multiple Failed Login Attempts
* Critical AI Alerts

#### MEDIUM Risk

Examples:

* Suspicious Access Attempts
* Reconnaissance Activities

#### LOW Risk

Examples:

* Informational Security Events
* Non-critical Activities

---

### 3. Real-Time Dashboard

The Streamlit dashboard updates automatically and provides:

* Total Alerts
* High Risk Alerts
* Medium Risk Alerts
* Low Risk Alerts

This allows security analysts to quickly assess the overall security status.

---

### 4. Attack Distribution Analysis

The dashboard visualizes:

* Brute Force Attacks
* AI Alerts
* Other Attack Categories

using interactive bar charts.

This helps identify the most common attack types.

---

### 5. Risk Breakdown Visualization

A pie chart displays the distribution of:

* HIGH Risk Alerts
* MEDIUM Risk Alerts
* LOW Risk Alerts

allowing quick threat assessment.

---

### 6. Attack Timeline

The system tracks attack activity over time and generates a timeline graph showing:

* Attack Frequency
* Security Event Trends
* Activity Peaks

This helps identify periods of increased malicious activity.

---

### 7. Top Attacking IP Addresses

The dashboard identifies the most active attacking IP addresses.

Benefits:

* Detect repeated attackers
* Identify suspicious hosts
* Support incident response investigations

---

### 8. Live Alert Feed

A real-time alert section displays the latest security events.

Alert colors indicate severity:

* Red → HIGH Risk
* Yellow → MEDIUM Risk
* Blue → LOW Risk

---

### 9. GeoIP Threat Intelligence

The system performs GeoIP lookups using the attacker's IP address.

Information collected:

* Country
* City
* Latitude
* Longitude

Example:

IP Address:
8.8.8.8

Location:
Mountain View, United States

---

### 10. Global Attack Mapping

Using Folium maps, attack locations are displayed worldwide.

Benefits:

* Visualize attack origins
* Understand geographic threat patterns
* Improve situational awareness

---

## Technologies Used

### Backend

* Python

### Database

* SQLite

### Dashboard

* Streamlit

### Data Processing

* Pandas

### Data Visualization

* Plotly

### Mapping

* Folium
* Streamlit-Folium

### GeoIP Services

* IP Geolocation API

---

## System Architecture

Log Sources
↓
Log Parser
↓
Attack Detection Engine
↓
Risk Classification
↓
GeoIP Lookup
↓
SQLite Database
↓
SOC Dashboard
↓
Charts • Alerts • Timeline • Maps

---

## Project Structure

project/

├── app.py

├── database.py

├── detector.py

├── geoip.py

├── security_logs.db

├── requirements.txt

└── README.md

---

## Installation

### Clone Repository

git clone <repository-url>

cd project

### Install Dependencies

pip install -r requirements.txt

### Run Application

streamlit run app.py

---

## Dashboard Components

* Security Metrics
* Attack Distribution Chart
* Risk Breakdown Chart
* Attack Timeline
* Top Attacking IPs
* Live Alert Feed
* GeoIP Attack Map
* Attack History Table

---

## Applications

This project can be used for:

* Cybersecurity Education
* Intrusion Detection Research
* Security Monitoring Demonstrations
* SOC Dashboard Development
* Threat Intelligence Visualization

---

## Future Enhancements

* Threat Intelligence Integration
* Email Notifications
* PDF Report Generation
* Machine Learning Based Threat Prediction
* SIEM Integration
* Log File Monitoring
* User Authentication

---

## Author

Developed as a Cyber Security and Intrusion Detection Project using Python and Streamlit.
