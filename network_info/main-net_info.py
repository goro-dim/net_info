from net_info import get_active_connections
from utils import extract_ips
from threat_intel import check_ip_threat


def main():
    connections = get_active_connections()
    ips = extract_ips(connections)

    for ip in ips:
        result = check_ip_threat(ip)
        print(f'IP: {ip} - Threat Info: {result}')


if __name__ == '__main__':
    main()
