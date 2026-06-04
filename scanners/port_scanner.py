from core.utils import command_exists, get_output


def scan_open_ports():
    if command_exists("ss"):
        output = get_output("ss -tulnp")
        source = "ss"
    elif command_exists("netstat"):
        output = get_output("netstat -tulnp")
        source = "netstat"
    else:
        return {
            "source": None,
            "message": "Neither ss nor netstat is installed. Cannot list open ports.",
            "ports": []
        }

    ports = []
    for line in output.splitlines():
        if not line or line.lower().startswith(("netid", "proto", "active")):
            continue

        ports.append(line)

    return {
        "source": source,
        "message": f"Collected open ports with {source}.",
        "ports": ports
    }


def print_open_ports():
    result = scan_open_ports()
    print("[*] Open Network Ports")
    print(result["message"])

    if not result["ports"]:
        return

    for port in result["ports"]:
        print(port)
