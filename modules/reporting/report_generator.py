import datetime
import os
from core.utils import get_output
from core.colors import GREEN, RESET


def generate_report():
    os.makedirs("reports/txt", exist_ok=True)

    report_file = "reports/txt/security_report.txt"

    with open(report_file, "w") as report:
        report.write("====================================\n")
        report.write("THREAT HUNTER SECURITY REPORT\n")
        report.write("====================================\n\n")

        report.write(f"Generated: {datetime.datetime.now()}\n\n")

        report.write("====================================\n")
        report.write("SYSTEM INFORMATION\n")
        report.write("====================================\n")
        report.write(get_output("hostnamectl"))

        report.write("\n\n====================================\n")
        report.write("OPEN NETWORK PORTS\n")
        report.write("====================================\n")
        report.write(get_output("ss -tuln"))

        report.write("\n\n====================================\n")
        report.write("RUNNING PROCESSES\n")
        report.write("====================================\n")
        report.write(get_output("ps aux --sort=-%mem | head -20"))

        report.write("\n\n====================================\n")
        report.write("FIREWALL STATUS\n")
        report.write("====================================\n")
        report.write(get_output("sudo ufw status"))

        report.write("\n\n====================================\n")
        report.write("LOGGED-IN USERS\n")
        report.write("====================================\n")
        report.write(get_output("who"))

        report.write("\n\n====================================\n")
        report.write("FAILED LOG / SYSTEM WARNINGS\n")
        report.write("====================================\n")
        report.write(
            get_output("journalctl --no-pager | grep -i 'failed' | tail -20")
        )

        report.write("\n\n====================================\n")
        report.write("END OF REPORT\n")
        report.write("====================================\n")

    print(f"{GREEN}Report saved:{RESET} {report_file}")
