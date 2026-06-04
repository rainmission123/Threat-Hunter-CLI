# Threat Hunter CLI

Threat Hunter CLI is a defensive Linux security auditing and incident response helper. It collects host information, reviews common security signals, runs lightweight threat-hunting checks, and writes reports in TXT, JSON, or HTML format.

The project is designed to run safely with:

```bash
python3 threat_hunter.py
```

## Features

- Linux system information review
- Open port listing with `ss` or `netstat`
- Running process review
- Firewall status check
- Logged-in user review
- Failed login and system warning review
- Suspicious process scanner with LOW, MEDIUM, and HIGH risk scoring
- File integrity hash collection for sensitive Linux files
- Suspicious file checks in temporary directories
- Basic rootkit indicator checks
- Optional `chkrootkit` and `rkhunter` support when installed
- VirusTotal hash lookup when an API key is configured
- Whois lookup when the `whois` command is installed
- TXT, JSON, and HTML report generation
- Friendly messages when optional tools are missing

## Installation

Clone the repository:

```bash
git clone https://github.com/rainmission123/Threat-Hunter-CLI.git
cd Threat-Hunter-CLI
```

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Optional Linux tools improve coverage:

```bash
sudo apt install whois ufw chkrootkit rkhunter net-tools
```

## API Keys

Copy the example config if you want to use external lookups:

```bash
cp config/api_keys.example.json config/api_keys.json
```

Then edit `config/api_keys.json`, or set environment variables:

```bash
export VIRUSTOTAL_API_KEY="your-key"
export ABUSEIPDB_API_KEY="your-key"
export SHODAN_API_KEY="your-key"
```

## Usage

Start the menu:

```bash
python3 threat_hunter.py
```

Choose a menu option to run a scanner or generate a report. Reports are saved under:

- `reports/txt/security_report.txt`
- `reports/json/security_report.json`
- `reports/html/security_report.html`

## Folder Structure

```text
Threat-Hunter-CLI/
├── config/
│   ├── api_keys.example.json
│   └── settings.json
├── core/
│   ├── colors.py
│   ├── logger.py
│   ├── menu.py
│   └── utils.py
├── integrations/
│   ├── abuseipdb.py
│   ├── shodan.py
│   ├── virustotal.py
│   └── whois_lookup.py
├── modules/
│   └── reporting/
│       └── report_generator.py
├── scanners/
│   ├── file_integrity.py
│   ├── port_scanner.py
│   ├── process_scanner.py
│   ├── rootkit_checker.py
│   ├── suspicious_files.py
│   └── yara_scanner.py
├── requirements.txt
└── threat_hunter.py
```

## Screenshots

Add screenshots here after running the tool in a Linux terminal.

Suggested captures:

- Main menu
- Suspicious process scanner output
- HTML report preview

## Defensive-Use Disclaimer

Threat Hunter CLI is for defensive security auditing, incident response, education, and authorized administration only. Do not use it on systems you do not own or do not have permission to assess. This project does not include malware, payload builders, backdoors, exploit delivery, credential theft, phishing, or unauthorized access features.
