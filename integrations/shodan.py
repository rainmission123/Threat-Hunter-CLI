import json
import os


API_URL = "https://api.shodan.io/shodan/host"


def get_api_key(config_path="config/api_keys.json"):
    env_key = os.environ.get("SHODAN_API_KEY")
    if env_key:
        return env_key

    if not os.path.exists(config_path):
        return None

    with open(config_path, "r", encoding="utf-8") as config:
        data = json.load(config)

    return data.get("shodan_api_key")


def lookup_host(ip_address, api_key=None):
    api_key = api_key or get_api_key()

    if not api_key:
        return {
            "status": "NO_API_KEY",
            "message": "Shodan API key not configured. Set SHODAN_API_KEY or config/api_keys.json."
        }

    try:
        import requests
    except ImportError:
        return {"status": "MISSING_DEPENDENCY", "message": "requests is not installed."}

    response = requests.get(f"{API_URL}/{ip_address}", params={"key": api_key}, timeout=20)

    if response.status_code == 404:
        return {"status": "NOT_FOUND", "message": "Host was not found in Shodan."}

    if response.status_code != 200:
        return {"status": "ERROR", "message": f"Shodan returned HTTP {response.status_code}."}

    data = response.json()
    return {
        "status": "OK",
        "message": "Shodan lookup completed.",
        "ip": data.get("ip_str"),
        "hostnames": data.get("hostnames", []),
        "ports": data.get("ports", []),
        "org": data.get("org"),
        "country": data.get("country_name")
    }


def print_shodan_lookup(ip_address):
    result = lookup_host(ip_address)
    print(result["message"])

    for key in ("ip", "org", "country", "hostnames", "ports"):
        if result.get(key):
            print(f"{key}: {result[key]}")
