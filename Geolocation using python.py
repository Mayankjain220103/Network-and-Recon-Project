# ip_geo_locator.py – IP Geolocation using public APIs
import requests
import argparse

def locate(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    for k, v in data.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IP Geolocation Tool')
    parser.add_argument('ip', help='IP Address to locate')
    args = parser.parse_args()
    locate(args.ip)
