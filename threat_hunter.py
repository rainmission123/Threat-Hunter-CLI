#!/usr/bin/env python3

from core.menu import show_header, show_menu
from core.utils import run_command, pause
from core.colors import GREEN, RED, RESET
from modules.reporting.report_generator import generate_report
from scanners.process_scanner import print_suspicious_processes


def main():
    while True:
        show_header()
        show_menu()

        choice = input("Select option: ")

        if choice == "1":
            run_command("hostnamectl")
            pause()

        elif choice == "2":
            run_command("ss -tulnp")
            pause()

        elif choice == "3":
            run_command("ps aux --sort=-%mem | head -20")
            pause()

        elif choice == "4":
            run_command("sudo ufw status")
            pause()

        elif choice == "5":
            run_command("who")
            pause()

        elif choice == "6":
            run_command("journalctl --no-pager | grep -i 'failed' | tail -20")
            pause()

        elif choice == "7":
            generate_report()
            pause()

        elif choice == "8":
            print_suspicious_processes()
            pause()

        elif choice == "0":
            print(f"{GREEN}Exiting Threat Hunter CLI...{RESET}")
            break

        else:
            print(f"{RED}Invalid option.{RESET}")
            pause()


if __name__ == "__main__":
    main()
