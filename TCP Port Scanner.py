TCP Port Scanner -  Scans a target host for open TCP ports.


### port_scanner.py – Lightweight Python port scanner

import socket
import argparse

def scan_host(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lightweight TCP port scanner')
    parser.add_argument('host', help='Target host to scan')
    parser.add_argument('--ports', help='Ports to scan, e.g. 22,80,443', default='1-1024')
    args = parser.parse_args()

    port_range = []
    if '-' in args.ports:
        start, end = map(int, args.ports.split('-'))
        port_range = range(start, end + 1)
    else:
        port_range = [int(p) for p in args.ports.split(',')]

    scan_host(args.host, port_range)
