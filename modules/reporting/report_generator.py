import datetime
import html
import json
import os

from core.colors import GREEN, RESET
from core.utils import run_optional_command
from scanners.file_integrity import scan_file_integrity
from scanners.port_scanner import scan_open_ports
from scanners.process_scanner import scan_suspicious_processes
from scanners.rootkit_checker import scan_rootkits
from scanners.suspicious_files import scan_suspicious_files


def collect_report_data():
    return {
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "system_information": run_optional_command("hostnamectl", "hostnamectl"),
        "open_ports": scan_open_ports(),
        "top_processes": run_optional_command("ps aux --sort=-%mem | head -20", "ps"),
        "firewall_status": run_optional_command("sudo ufw status", "ufw"),
        "logged_in_users": run_optional_command("who", "who"),
        "failed_login_attempts": run_optional_command(
            "journalctl --no-pager | grep -i 'failed' | tail -20",
            "journalctl"
        ),
        "suspicious_processes": scan_suspicious_processes(),
        "file_integrity": scan_file_integrity(),
        "suspicious_files": scan_suspicious_files(),
        "rootkit_checks": scan_rootkits(),
    }


def generate_report(format_type="txt"):
    format_type = format_type.lower()
    data = collect_report_data()

    if format_type == "json":
        report_file = _write_json_report(data)
    elif format_type == "html":
        report_file = _write_html_report(data)
    else:
        report_file = _write_txt_report(data)

    print(f"{GREEN}Report saved:{RESET} {report_file}")
    return report_file


def _write_txt_report(data):
    os.makedirs("reports/txt", exist_ok=True)
    report_file = "reports/txt/security_report.txt"

    with open(report_file, "w", encoding="utf-8") as report:
        report.write("====================================\n")
        report.write("THREAT HUNTER SECURITY REPORT\n")
        report.write("====================================\n\n")
        report.write(f"Generated: {data['generated_at']}\n\n")

        _write_txt_section(report, "SYSTEM INFORMATION", data["system_information"])
        _write_txt_section(report, "OPEN NETWORK PORTS", "\n".join(data["open_ports"]["ports"]) or data["open_ports"]["message"])
        _write_txt_section(report, "RUNNING PROCESSES", data["top_processes"])
        _write_txt_section(report, "FIREWALL STATUS", data["firewall_status"])
        _write_txt_section(report, "LOGGED-IN USERS", data["logged_in_users"])
        _write_txt_section(report, "FAILED LOG / SYSTEM WARNINGS", data["failed_login_attempts"])
        _write_txt_section(report, "SUSPICIOUS PROCESSES", _format_list(data["suspicious_processes"]))
        _write_txt_section(report, "FILE INTEGRITY", _format_list(data["file_integrity"]))
        _write_txt_section(report, "SUSPICIOUS FILES", _format_list(data["suspicious_files"]))
        _write_txt_section(report, "ROOTKIT CHECKS", _format_dict(data["rootkit_checks"]))

        report.write("\n====================================\n")
        report.write("END OF REPORT\n")
        report.write("====================================\n")

    return report_file


def _write_json_report(data):
    os.makedirs("reports/json", exist_ok=True)
    report_file = "reports/json/security_report.json"

    with open(report_file, "w", encoding="utf-8") as report:
        json.dump(data, report, indent=2)

    return report_file


def _write_html_report(data):
    os.makedirs("reports/html", exist_ok=True)
    report_file = "reports/html/security_report.html"

    sections = [
        ("System Information", data["system_information"]),
        ("Open Network Ports", data["open_ports"]),
        ("Running Processes", data["top_processes"]),
        ("Firewall Status", data["firewall_status"]),
        ("Logged-in Users", data["logged_in_users"]),
        ("Failed Login Attempts", data["failed_login_attempts"]),
        ("Suspicious Processes", data["suspicious_processes"]),
        ("File Integrity", data["file_integrity"]),
        ("Suspicious Files", data["suspicious_files"]),
        ("Rootkit Checks", data["rootkit_checks"]),
    ]

    with open(report_file, "w", encoding="utf-8") as report:
        report.write("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Threat Hunter Security Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; color: #1f2937; }
    h1 { color: #111827; }
    section { border-top: 1px solid #d1d5db; padding: 1rem 0; }
    pre { background: #f3f4f6; padding: 1rem; overflow-x: auto; }
  </style>
</head>
<body>
""")
        report.write("<h1>Threat Hunter Security Report</h1>\n")
        report.write(f"<p>Generated: {html.escape(data['generated_at'])}</p>\n")

        for title, content in sections:
            report.write("<section>\n")
            report.write(f"<h2>{html.escape(title)}</h2>\n")
            report.write(f"<pre>{html.escape(_to_text(content))}</pre>\n")
            report.write("</section>\n")

        report.write("</body>\n</html>\n")

    return report_file


def _write_txt_section(report, title, content):
    report.write("\n====================================\n")
    report.write(f"{title}\n")
    report.write("====================================\n")
    report.write(_to_text(content))
    report.write("\n")


def _format_list(items):
    if not items:
        return "No findings."

    return "\n".join(_format_dict(item) for item in items)


def _format_dict(item):
    return json.dumps(item, indent=2)


def _to_text(content):
    if isinstance(content, str):
        return content

    return json.dumps(content, indent=2)
