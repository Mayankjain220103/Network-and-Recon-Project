# dns_enum.sh – Bash script for DNS enumeration
#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <domain>"
  exit 1
fi

domain=$1
wordlist="/usr/share/wordlists/dns.txt"

echo "[+] A Record Lookup"
dig +short A $domain

echo "[+] NS Records"
dig +short NS $domain

echo "[+] MX Records"
dig +short MX $domain

echo "[+] Subdomain Brute-force using $wordlist"
for sub in $(cat $wordlist); do
  host "$sub.$domain" | grep -v "not found"
done
