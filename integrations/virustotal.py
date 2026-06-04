import hashlib
import json
import os


API_URL = "https://www.virustotal.com/api/v3/files"


def get_api_key(config_path="config/api_keys.json"):
    env_key = os.environ.get("VIRUSTOTAL_API_KEY")
    if env_key:
        return env_key

    if not os.path.exists(config_path):
        return None

    with open(config_path, "r", encoding="utf-8") as config:
        data = json.load(config)

    return data.get("virustotal_api_key")


def file_sha256(path):
    digest = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)

    return digest.hexdigest()


def lookup_file_hash(file_hash, api_key=None):
    api_key = api_key or get_api_key()

    if not api_key:
        return {
            "status": "NO_API_KEY",
            "message": "VirusTotal API key not configured. Set VIRUSTOTAL_API_KEY or config/api_keys.json."
        }

    try:
        import requests
    except ImportError:
        return {
            "status": "MISSING_DEPENDENCY",
            "message": "requests is not installed."
        }

    response = requests.get(
        f"{API_URL}/{file_hash}",
        headers={"x-apikey": api_key},
        timeout=20
    )

    if response.status_code == 404:
        return {"status": "NOT_FOUND", "message": "Hash was not found in VirusTotal."}

    if response.status_code != 200:
        return {"status": "ERROR", "message": f"VirusTotal returned HTTP {response.status_code}."}

    stats = response.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
    return {
        "status": "OK",
        "message": "VirusTotal lookup completed.",
        "stats": stats
    }


def print_virustotal_lookup(value):
    if os.path.exists(value) and os.path.isfile(value):
        value = file_sha256(value)

    result = lookup_file_hash(value)
    print(result["message"])

    if result.get("stats"):
        for key, count in result["stats"].items():
            print(f"{key}: {count}")
