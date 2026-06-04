import os
import stat


DEFAULT_SCAN_PATHS = [
    "/tmp",
    "/var/tmp",
    "/dev/shm",
]

SUSPICIOUS_NAMES = [
    ".ssh",
    "backdoor",
    "payload",
    "miner",
    "xmrig",
    "nc",
    "ncat",
    "netcat",
]


def score_file(path, mode):
    name = os.path.basename(path).lower()
    score = 0
    reasons = []

    if name.startswith(".") and stat.S_ISREG(mode):
        score += 1
        reasons.append("hidden file")

    if any(keyword == name or keyword in name for keyword in SUSPICIOUS_NAMES):
        score += 2
        reasons.append("suspicious name")

    if mode & stat.S_IXUSR and stat.S_ISREG(mode):
        score += 1
        reasons.append("executable file")

    if mode & stat.S_ISUID:
        score += 3
        reasons.append("setuid bit")

    if mode & stat.S_IWOTH:
        score += 1
        reasons.append("world-writable")

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, reasons


def scan_suspicious_files(paths=None, max_files=5000):
    paths = paths or DEFAULT_SCAN_PATHS
    findings = []
    inspected = 0

    for base_path in paths:
        if not os.path.exists(base_path):
            continue

        for root, _, files in os.walk(base_path):
            for filename in files:
                if inspected >= max_files:
                    return findings

                inspected += 1
                path = os.path.join(root, filename)

                try:
                    file_stat = os.lstat(path)
                except OSError:
                    continue

                risk, reasons = score_file(path, file_stat.st_mode)
                if reasons:
                    findings.append({
                        "risk": risk,
                        "path": path,
                        "reasons": reasons
                    })

    return findings


def print_suspicious_files():
    findings = scan_suspicious_files()

    if not findings:
        print("[OK] No suspicious files found in default temporary paths.")
        return

    print("[WARNING] Suspicious files found:")
    for item in findings:
        print(f"[{item['risk']}] {item['path']}")
        print(f"  Reasons: {', '.join(item['reasons'])}")
