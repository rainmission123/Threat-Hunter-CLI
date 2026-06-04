import os
import shutil
import subprocess
from core.colors import RED, CYAN, RESET


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


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
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
    except Exception as error:
        return f"Error running command: {error}"

    output = result.stdout.strip()
    error = result.stderr.strip()

    if output:
        return output

    if error:
        return error

    return "No output."


def command_exists(command):
    return shutil.which(command) is not None


def run_optional_command(command, required_binary=None):
    binary = required_binary or command.split()[0]

    if not command_exists(binary):
        return f"{binary} is not installed or not available in PATH."

    return get_output(command)


def pause():
    input(f"\n{CYAN}Press Enter to continue...{RESET}")
