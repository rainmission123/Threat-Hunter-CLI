import json
import os


API_URL = "https://api.abuseipdb.com/api/v2/check"


def get_api_key(config_path="config/api_keys.json"):
    env_key = os.environ.get("ABUSEIPDB_API_KEY")
    if env_key:
        return env_key

    if not os.path.exists(config_path):
        return None

    with open(config_path, "r", encoding="utf-8") as config:
        data = json.load(config)

    return data.get("abuseipdb_api_key")


def lookup_ip(ip_address, api_key=None):
    api_key = api_key or get_api_key()

    if not api_key:
        return {
            "status": "NO_API_KEY",
            "message": "AbuseIPDB API key not configured. Set ABUSEIPDB_API_KEY or config/api_keys.json."
        }

    try:
        import requests
    except ImportError:
        return {"status": "MISSING_DEPENDENCY", "message": "requests is not installed."}

    response = requests.get(
        API_URL,
        headers={"Key": api_key, "Accept": "application/json"},
        params={"ipAddress": ip_address, "maxAgeInDays": 90},
        timeout=20
    )

    if response.status_code != 200:
        return {"status": "ERROR", "message": f"AbuseIPDB returned HTTP {response.status_code}."}

    data = response.json().get("data", {})
    return {
        "status": "OK",
        "message": "AbuseIPDB lookup completed.",
        "ip": data.get("ipAddress"),
        "abuse_confidence_score": data.get("abuseConfidenceScore"),
        "country": data.get("countryCode"),
        "usage_type": data.get("usageType")
    }


def print_abuseipdb_lookup(ip_address):
    result = lookup_ip(ip_address)
    print(result["message"])

    for key in ("ip", "abuse_confidence_score", "country", "usage_type"):
        if result.get(key) is not None:
            print(f"{key}: {result[key]}")
