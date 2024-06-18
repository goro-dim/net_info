import re

def extract_ips(connections):
    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    ips = set()
    for line in connections:
        matches = ip_pattern.findall(line)
        ips.update(matches)
    return list(ips)
