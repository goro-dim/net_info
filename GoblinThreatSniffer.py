#!/usr/bin/env python3
# GoblinThreatSniffer.py

import sys
import os
from NetworkSeeker import gather_network_info
from ThreatInspector import query_abuseipdb
from OutputDecorator import format_output

API_KEY = 'your_abuseipdb_api_key_here'  # Replace with your AbuseIPDB API key

def usage():
    print("🧌 GoblinThreatSniffer Usage:")
    print("  python3 GoblinThreatSniffer.py <ip>")
    print("  python3 GoblinThreatSniffer.py -f <file_with_ips>")
    print("  python3 GoblinThreatSniffer.py --help")

def scan_ip(ip):
    info = query_abuseipdb(API_KEY, ip)
    output = format_output(ip, info)
    print(output)
    print("-" * 50)

def scan_from_file(filepath):
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filepath}")
        return

    with open(filepath, "r") as f:
        ips = [line.strip() for line in f if line.strip()]

    if not ips:
        print("[!] No IPs found in file.")
        return

    print(f"[~] Scanning {len(ips)} IPs from {filepath}...")
    for ip in ips:
        scan_ip(ip)

def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        usage()
        sys.exit()

    if argv[0] in ("-f", "--file"):
        if len(argv) < 2:
            print("[!] Missing file path after -f")
            sys.exit(2)
        filepath = argv[1]
        scan_from_file(filepath)

    else:
        ip = argv[0]
        scan_ip(ip)

if __name__ == "__main__":
    main(sys.argv[1:])
