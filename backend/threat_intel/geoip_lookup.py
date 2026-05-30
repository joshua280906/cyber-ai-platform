import requests

# ---------------------------------------------------
# GEOLOCATION LOOKUP
# ---------------------------------------------------

def lookup_ip(ip):

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

    except Exception:

        return {

            "country": "Unknown",

            "city": "Unknown",

            "lat": 0,

            "lon": 0
        }