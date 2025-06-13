🔧 Cybersecurity Recon & Enumeration Tools

A collection of lightweight and powerful Python & Bash tools for reconnaissance, enumeration, and information gathering in cybersecurity assessments. Ideal for bug bounty hunters, penetration testers, and ethical hackers.

📁 Tools Included

1. port_scanner.py – 🚪 TCP Port Scanner

Features:

🔎 Scans custom or default port ranges on target host

⚡ Fast scanning using socket timeouts

💡 Identifies open TCP ports to map running services

🧩 Great for enumeration during network recon

Usage:

python3 port_scanner.py <host> --ports 1-1024
python3 port_scanner.py example.com --ports 80,443,8080

2. dns_enum.sh – 🌐 DNS Enumeration Tool

Features:

📡 A, MX, and NS record lookups

🧰 Brute-force subdomain discovery using wordlists

🔐 Identifies DNS misconfigurations or exposed records

🧠 Useful for red teaming and initial recon

Usage:

chmod +x dns_enum.sh
./dns_enum.sh example.com

Ensure /usr/share/wordlists/dns.txt exists or update with your own path.

3. whois_lookup.py – 🔍 WHOIS Lookup Tool

Features:

📋 Retrieves domain/IP registration data (e.g., registrar, creation date, expiry)

🧠 OSINT-friendly for target footprinting

🛠️ Supports both domains and IPs

🚫 Handles private or missing WHOIS gracefully

Usage:

python3 whois_lookup.py example.com

4. ip_geo_locator.py – 🗺️ IP Geolocation Tool

Features:

🌍 Uses ip-api.com to fetch real-time geolocation

📌 Outputs country, region, city, ISP, lat/lon, timezone

🚦 Lightweight and fast for IP tracking tasks

🧰 Useful for identifying attacker infrastructure or foreign connections

Usage:

python3 ip_geo_locator.py 8.8.8.8



📌 Requirements

Python 3.x

Bash shell

Dependencies: fping, arp-scan, dig, host, whois, requests, python-whois

📦 Install Python packages:

pip install requests python-whois

📂 Directory Structure

.
├── dns_enum.sh
├── ip_geo_locator.py
├── port_scanner.py
├── whois_lookup.py
└── README.md

⚠️ Disclaimer

These tools are for educational and authorized testing purposes only. Unauthorized use is strictly prohibited and may be illegal.

🙌 Contributions

Pull Requests are welcome! Enhance existing tools, add more recon modules, or help improve documentation.

👨‍💻 Author

Maintained by Mayank Jain – Passionate about Cybersecurity & Open Source.

⭐ Support

If you find this project helpful, please star 🌟 the repo and share it with fellow cybersecurity learners!

