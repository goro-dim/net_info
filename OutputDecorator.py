# OutputDecorator.py

def format_output(ip, info):
    if 'error' in info:
        return f"Error: {info['error']}"

    if info['data']['abuseConfidenceScore'] > 30:
        threat_level = "High"
    elif info['data']['abuseConfidenceScore'] > 10:
        threat_level = "Medium"
    else:
        threat_level = "Low"

    output = f"IP: {ip} - Threat Level: {threat_level}\n"
    output += f"    Country: {info['data']['countryCode']}\n"
    output += f"    ISP: {info['data']['isp']}\n"
    output += f"    Usage Type: {info['data']['usageType']}\n"
    output += f"    Last Reported: {info['data']['lastReportedAt']}\n"

    return output
