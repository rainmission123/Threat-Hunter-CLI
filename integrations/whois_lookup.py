import subprocess

from core.utils import command_exists


def lookup_whois(target):
    if not command_exists("whois"):
        return {
            "status": "MISSING_TOOL",
            "message": "whois is not installed. Install the whois package to enable lookups.",
            "output": ""
        }

    try:
        result = subprocess.run(
            ["whois", target],
            text=True,
            capture_output=True,
            timeout=30
        )
    except Exception as error:
        return {
            "status": "ERROR",
            "message": f"Whois lookup failed: {error}",
            "output": ""
        }

    output = result.stdout.strip() or result.stderr.strip()

    return {
        "status": "OK",
        "message": "Whois lookup completed.",
        "output": output
    }


def print_whois_lookup(target):
    result = lookup_whois(target)
    print(result["message"])

    if result["output"]:
        print(result["output"])
