import subprocess


SUSPICIOUS_KEYWORDS = [
    "nc",
    "netcat",
    "ncat",
    "socat",
    "meterpreter",
    "msfvenom",
    "payload",
    "backdoor",
    "reverse",
    "bind",
    "cryptominer",
    "xmrig",
    "minerd",
    "hydra",
    "john",
    "hashcat",
    "sqlmap",
    "nikto",
    "nmap"
]


def get_processes():
    result = subprocess.run(
        "ps aux",
        shell=True,
        text=True,
        capture_output=True
    )

    return result.stdout.splitlines()


def scan_suspicious_processes():
    processes = get_processes()
    findings = []

    for process in processes[1:]:
        lower_process = process.lower()

        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in lower_process:
                findings.append({
                    "keyword": keyword,
                    "process": process
                })

    return findings


def print_suspicious_processes():
    findings = scan_suspicious_processes()

    if not findings:
        print("[OK] No suspicious processes found.")
        return

    print("[WARNING] Suspicious processes found:\n")

    for item in findings:
        print(f"Keyword: {item['keyword']}")
        print(f"Process: {item['process']}")
        print("-" * 60)
