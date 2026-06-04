import os


def scan_with_yara(target_path, rules_path):
    try:
        import yara
    except ImportError:
        return {
            "status": "MISSING_DEPENDENCY",
            "message": "yara-python is not installed. Install it only if you need YARA scanning.",
            "matches": []
        }

    if not os.path.exists(target_path):
        return {
            "status": "ERROR",
            "message": f"Target path not found: {target_path}",
            "matches": []
        }

    if not os.path.exists(rules_path):
        return {
            "status": "ERROR",
            "message": f"YARA rules file not found: {rules_path}",
            "matches": []
        }

    rules = yara.compile(filepath=rules_path)
    matches = []

    if os.path.isfile(target_path):
        matches.extend(_scan_file(rules, target_path))
    else:
        for root, _, files in os.walk(target_path):
            for filename in files:
                matches.extend(_scan_file(rules, os.path.join(root, filename)))

    return {
        "status": "OK",
        "message": "YARA scan completed.",
        "matches": matches
    }


def _scan_file(rules, path):
    try:
        matches = rules.match(path)
    except Exception:
        return []

    return [
        {
            "file": path,
            "rule": str(match)
        }
        for match in matches
    ]


def print_yara_scan(target_path, rules_path):
    result = scan_with_yara(target_path, rules_path)
    print(result["message"])

    for match in result["matches"]:
        print(f"{match['file']}: {match['rule']}")
