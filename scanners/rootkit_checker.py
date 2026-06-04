import os

from core.utils import command_exists, get_output


SUSPICIOUS_PATHS = [
    "/tmp/.X11-unix/...",
    "/tmp/.ICE-unix/...",
    "/usr/bin/...",
    "/usr/sbin/...",
    "/var/tmp/...",
]


def run_rootkit_tools():
    results = []

    if command_exists("chkrootkit"):
        results.append({
            "tool": "chkrootkit",
            "status": "RAN",
            "output": get_output("chkrootkit")
        })
    else:
        results.append({
            "tool": "chkrootkit",
            "status": "MISSING",
            "output": "chkrootkit is not installed."
        })

    if command_exists("rkhunter"):
        results.append({
            "tool": "rkhunter",
            "status": "RAN",
            "output": get_output("rkhunter --check --skip-keypress --report-warnings-only")
        })
    else:
        results.append({
            "tool": "rkhunter",
            "status": "MISSING",
            "output": "rkhunter is not installed."
        })

    return results


def basic_rootkit_checks():
    findings = []

    for path in SUSPICIOUS_PATHS:
        if os.path.exists(path):
            findings.append({
                "risk": "MEDIUM",
                "path": path,
                "message": "Suspicious hidden path exists. Review manually."
            })

    if os.path.exists("/proc") and os.path.exists("/bin/ps"):
        findings.append({
            "risk": "LOW",
            "path": "/proc",
            "message": "Basic process visibility check available. Use chkrootkit/rkhunter for deeper checks."
        })

    return findings


def scan_rootkits():
    return {
        "tool_results": run_rootkit_tools(),
        "basic_findings": basic_rootkit_checks()
    }


def print_rootkit_check():
    result = scan_rootkits()
    print("[*] Rootkit Checker")

    for item in result["tool_results"]:
        print(f"{item['tool']}: {item['status']}")
        if item["status"] == "MISSING":
            print(f"  {item['output']}")

    if not result["basic_findings"]:
        print("[OK] No suspicious rootkit indicators found in basic checks.")
        return

    for finding in result["basic_findings"]:
        print(f"[{finding['risk']}] {finding['path']}: {finding['message']}")
