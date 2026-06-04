#!/usr/bin/env python3

from core.menu import show_header, show_menu
from core.utils import run_optional_command, pause
from core.colors import GREEN, RED, RESET
from integrations.virustotal import print_virustotal_lookup
from integrations.whois_lookup import print_whois_lookup
from modules.reporting.report_generator import generate_report
from scanners.file_integrity import print_file_integrity
from scanners.port_scanner import print_open_ports
from scanners.process_scanner import print_suspicious_processes
from scanners.rootkit_checker import print_rootkit_check
from scanners.suspicious_files import print_suspicious_files


def main():
    while True:
        show_header()
        show_menu()

        choice = input("Select option: ").strip()

        if choice == "1":
            print(run_optional_command("hostnamectl", "hostnamectl"))
            pause()

        elif choice == "2":
            print_open_ports()
            pause()

        elif choice == "3":
            print(run_optional_command("ps aux --sort=-%mem | head -20", "ps"))
            pause()

        elif choice == "4":
            print(run_optional_command("sudo ufw status", "ufw"))
            pause()

        elif choice == "5":
            print(run_optional_command("who", "who"))
            pause()

        elif choice == "6":
            print(run_optional_command(
                "journalctl --no-pager | grep -i 'failed' | tail -20",
                "journalctl"
            ))
            pause()

        elif choice == "7":
            generate_report("txt")
            pause()

        elif choice == "8":
            print_suspicious_processes()
            pause()

        elif choice == "9":
            print_file_integrity()
            pause()

        elif choice == "10":
            print_suspicious_files()
            pause()

        elif choice == "11":
            print_rootkit_check()
            pause()

        elif choice == "12":
            value = input("Enter file path or SHA256 hash: ").strip()
            print_virustotal_lookup(value)
            pause()

        elif choice == "13":
            target = input("Enter domain or IP address: ").strip()
            print_whois_lookup(target)
            pause()

        elif choice == "14":
            generate_report("json")
            pause()

        elif choice == "15":
            generate_report("html")
            pause()

        elif choice == "0":
            print(f"{GREEN}Exiting Threat Hunter CLI...{RESET}")
            break

        else:
            print(f"{RED}Invalid option.{RESET}")
            pause()


if __name__ == "__main__":
    main()
