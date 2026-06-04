from core.colors import GREEN, CYAN, YELLOW, RESET
from core.utils import clear_screen


def show_header():
    clear_screen()

    print(f"""{GREEN}
============================================================
 THREAT HUNTER CLI
============================================================
{CYAN}Threat Hunter CLI v0.2 Alpha
Linux Security Audit & Threat Detection Tool
{RESET}""")


def show_menu():
    print(f"{YELLOW}[1]{RESET} System Information")
    print(f"{YELLOW}[2]{RESET} Open Network Ports")
    print(f"{YELLOW}[3]{RESET} Running Processes")
    print(f"{YELLOW}[4]{RESET} Firewall Status")
    print(f"{YELLOW}[5]{RESET} Logged-in Users")
    print(f"{YELLOW}[6]{RESET} Failed Login Attempts")
    print(f"{YELLOW}[7]{RESET} Generate TXT Security Report")
    print(f"{YELLOW}[8]{RESET} Suspicious Process Scanner")
    print(f"{YELLOW}[9]{RESET} File Integrity Scanner")
    print(f"{YELLOW}[10]{RESET} Suspicious Files Scanner")
    print(f"{YELLOW}[11]{RESET} Rootkit Checker")
    print(f"{YELLOW}[12]{RESET} VirusTotal File/Hash Lookup")
    print(f"{YELLOW}[13]{RESET} Whois Lookup")
    print(f"{YELLOW}[14]{RESET} Generate JSON Security Report")
    print(f"{YELLOW}[15]{RESET} Generate HTML Security Report")
    print(f"{YELLOW}[0]{RESET} Exit")
    print("")
