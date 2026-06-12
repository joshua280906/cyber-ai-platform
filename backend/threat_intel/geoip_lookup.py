import requests

# ---------------------------------------------------
# GEOLOCATION LOOKUP
# ---------------------------------------------------

def lookup_ip(ip):

    # --------------------------------------------
    # PRIVATE / LOCAL IP FILTERING
    # --------------------------------------------

    private_prefixes = (

        "10.",
        "192.168.",
        "172.",
        "127."
    )

    if ip.startswith(private_prefixes):

        return {

            "country": "Private Network",

            "city": "Local",

            "lat": 0,

            "lon": 0
        }

    # --------------------------------------------
    # PUBLIC IP LOOKUP
    # --------------------------------------------

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