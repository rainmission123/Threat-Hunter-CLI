import os
import subprocess
from core.colors import RED, CYAN, RESET


def clear_screen():
    os.system("clear")


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )

        print(result.stdout)

        if result.stderr:
            print(f"{RED}{result.stderr}{RESET}")

    except Exception as error:
        print(f"{RED}Error: {error}{RESET}")


def get_output(command):
    return subprocess.getoutput(command)


def pause():
    input(f"\n{CYAN}Press Enter to continue...{RESET}")
