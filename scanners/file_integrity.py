import hashlib
import os


DEFAULT_PATHS = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/group",
    "/etc/sudoers",
    "/etc/ssh/sshd_config",
]


def hash_file(path, algorithm="sha256"):
    digest = hashlib.new(algorithm)

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)

    return digest.hexdigest()


def scan_file_integrity(paths=None):
    findings = []
    paths = paths or DEFAULT_PATHS

    for path in paths:
        item = {"path": path, "exists": os.path.exists(path)}

        if not item["exists"]:
            item["status"] = "MISSING"
            item["message"] = "File was not found on this system."
            findings.append(item)
            continue

        if not os.path.isfile(path):
            item["status"] = "SKIPPED"
            item["message"] = "Path is not a regular file."
            findings.append(item)
            continue

        try:
            item["sha256"] = hash_file(path)
            item["status"] = "OK"
            item["message"] = "Hash collected."
        except PermissionError:
            item["status"] = "PERMISSION_DENIED"
            item["message"] = "Permission denied. Try running with appropriate read access."
        except OSError as error:
            item["status"] = "ERROR"
            item["message"] = str(error)

        findings.append(item)

    return findings


def print_file_integrity(paths=None):
    print("[*] File Integrity Scanner")

    for item in scan_file_integrity(paths):
        print(f"{item['status']}: {item['path']}")
        if item.get("sha256"):
            print(f"  sha256: {item['sha256']}")
        print(f"  {item['message']}")
