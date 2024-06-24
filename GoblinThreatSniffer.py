#!/usr/bin/env python3
# GoblinThreatSniffer.py

import sys
import getopt
from NetworkSeeker import gather_network_info
from ThreatInspector import query_abuseipdb
from OutputDecorator import format_output

API_KEY = 'your_abuseipdb_api_key_here'  # Replace with your AbuseIPDB API key

def usage():
    print("Usage:")
    print("python3 GoblinThreatSniffer.py [-h] [<ip_address>]")

def main(argv):
    if len(argv) == 0:
        usage()
        sys.exit(2)

    ip = argv[0]

    if ip in ("-h", "--help"):
        usage()
        sys.exit()

    if ip:
        info = query_abuseipdb(API_KEY, ip)
        output = format_output(ip, info)
        print(output)
        print("-" * 50)
    else:
        connections = gather_network_info()
        for connection in connections:
            ip = connection['ip']
            info = query_abuseipdb(API_KEY, ip)
            output = format_output(ip, info)
            print(output)
            print("-" * 50)

if __name__ == "__main__":
    main(sys.argv[1:])
