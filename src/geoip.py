# geoip.py

import requests


def get_location(ip):

    try:

        response = requests.get(
            f"http://ip-api.com/json/{ip}"
        )

        data = response.json()

        return {
            "country": data.get("country"),
            "city": data.get("city"),
            "lat": data.get("lat"),
            "lon": data.get("lon")
        }

    except:

        return {
            "country": "Unknown",
            "city": "Unknown",
            "lat": None,
            "lon": None
        }