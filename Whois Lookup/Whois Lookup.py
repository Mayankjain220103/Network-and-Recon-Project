# whois_lookup.py – Automates WHOIS lookups
import whois
import argparse

def lookup(domain):
    try:
        info = whois.whois(domain)
        print(info)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WHOIS Lookup Tool')
    parser.add_argument('domain', help='Domain or IP')
    args = parser.parse_args()
    lookup(args.domain)
