import subprocess
import shlex


EXACT_PROCESS_NAMES = {
    "nc": 3,
    "ncat": 3,
    "netcat": 3,
    "socat": 2,
    "meterpreter": 4,
    "msfvenom": 4,
    "xmrig": 4,
    "minerd": 4,
    "hydra": 3,
    "john": 2,
    "hashcat": 2,
    "sqlmap": 2,
    "nikto": 2,
    "nmap": 1,
}

SUSPICIOUS_ARGUMENTS = {
    "reverse": 2,
    "bind": 2,
    "backdoor": 3,
    "payload": 3,
    "cryptominer": 4,
    "/dev/tcp": 3,
}


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
        finding = score_process(process)
        if finding:
            findings.append(finding)

    return findings


def score_process(process_line):
    parts = process_line.split(None, 10)

    if len(parts) < 11:
        return None

    command = parts[10]
    tokens = _split_command(command)

    if not tokens:
        return None

    executable = tokens[0].split("/")[-1].lower()
    command_lower = command.lower()
    score = 0
    reasons = []

    if executable in EXACT_PROCESS_NAMES:
        score += EXACT_PROCESS_NAMES[executable]
        reasons.append(f"process name: {executable}")

    for keyword, weight in SUSPICIOUS_ARGUMENTS.items():
        if keyword in command_lower:
            score += weight
            reasons.append(f"argument contains: {keyword}")

    if executable in {"nc", "ncat", "netcat", "socat"} and any(token in tokens for token in ("-e", "-c")):
        score += 4
        reasons.append("network utility executing a command")

    if score == 0:
        return None

    if score >= 5:
        risk = "HIGH"
    elif score >= 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "process": process_line
    }


def _split_command(command):
    try:
        return shlex.split(command)
    except ValueError:
        return command.split()


def print_suspicious_processes():
    findings = scan_suspicious_processes()

    if not findings:
        print("[OK] No suspicious processes found.")
        return

    print("[WARNING] Suspicious processes found:\n")

    for item in findings:
        print(f"Risk: {item['risk']} (score: {item['score']})")
        print(f"Reasons: {', '.join(item['reasons'])}")
        print(f"Process: {item['process']}")
        print("-" * 60)
