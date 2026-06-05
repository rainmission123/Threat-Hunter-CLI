<img width="1910" height="1172" alt="17143bf7-6a3d-4349-87fb-d6af7c9f1eb2" src="https://github.com/user-attachments/assets/3a8b6dd4-49b4-4a4b-b2ac-dcd42b288d36" />

A Linux-based Cyber Security and Threat Hunting Toolkit built with Python.

Threat Hunter CLI is designed for cybersecurity students, SOC analysts, blue team operators, security researchers, and IT professionals who want to perform security auditing, threat hunting, incident response, and threat intelligence investigations directly from the Linux terminal.

---

## 🚀 Features

### 🔍 System Monitoring

* System Information
* Open Network Ports Detection
* Running Process Enumeration
* Logged-In User Monitoring
* Failed Login Attempt Detection
* Firewall Status Monitoring

### 🕵️ Threat Hunting

* Suspicious Process Scanner
* Rootkit Detection
* File Integrity Monitoring
* Suspicious File Scanner
* Security Audit Checks

### 🌐 Threat Intelligence

* VirusTotal File & Hash Lookup
* AbuseIPDB Reputation Lookup
* Shodan Host Intelligence Lookup
* Whois Domain & IP Lookup

### 📄 Reporting

* Generate TXT Security Reports
* Generate JSON Security Reports
* Generate HTML Security Reports

---

## 🐧 Installation (Linux)

### Clone the Repository

```bash
git clone https://github.com/rainmission123/Threat-Hunter-CLI.git

cd Threat-Hunter-CLI
```

### Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Required Dependencies

```bash
sudo apt install python3 python3-pip net-tools curl whois -y
```

### Install Python Requirements

```bash
pip3 install -r requirements.txt
```

---

## 🔑 Configure API Keys

Create the API configuration file:

```bash
cp config/api_keys.example.json config/api_keys.json
```

Edit the file:

```bash
nano config/api_keys.json
```

Replace the placeholders with your actual API keys:

```json
{
  "virustotal_api_key": "YOUR_VIRUSTOTAL_API_KEY",
  "abuseipdb_api_key": "YOUR_ABUSEIPDB_API_KEY",
  "shodan_api_key": "YOUR_SHODAN_API_KEY"
}
```

Save and exit:

```text
CTRL + O
ENTER
CTRL + X
```

---

## ▶️ Running Threat Hunter CLI

Run directly with Python:

```bash
python3 threat_hunter.py
```

Or run using the launcher script:

```bash
chmod +x threat_hunter.sh

./threat_hunter.sh
```

---

## 📋 Main Menu

Current menu options include:

1. System Information
2. Open Network Ports
3. Running Processes
4. Firewall Status
5. Logged-In Users
6. Failed Login Attempts
7. Generate TXT Security Report
8. Suspicious Process Scanner
9. File Integrity Scanner
10. Suspicious File Scanner
11. Rootkit Checker
12. VirusTotal File/Hash Lookup
13. Whois Lookup
14. Generate JSON Security Report
15. Generate HTML Security Report
16. Exit

---

## 🌐 Integrated Services

| Service    | Purpose                        | Status |
| ---------- | ------------------------------ | ------ |
| VirusTotal | Malware & Hash Analysis        | ✅      |
| AbuseIPDB  | IP Reputation Analysis         | ✅      |
| Shodan     | Internet Exposure Intelligence | ✅      |
| Whois      | Domain & IP Ownership Lookup   | ✅      |

---

## 🛠️ Technologies Used

* Python 3
* Linux
* VirusTotal API
* AbuseIPDB API
* Shodan API
* Whois

---

## 🎯 Use Cases

* Security Auditing
* Threat Hunting
* Incident Response
* Malware Investigation
* IOC Analysis
* Cybersecurity Learning
* SOC Analyst Training

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rian Mission Llanos**

Cyber Security Enthusiast • Threat Hunter • Android Engineer

GitHub:
https://github.com/rainmission123

