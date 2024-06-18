import requests

def check_ip_threat(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {
        'Key': 'YOUR_API_KEY',# Replace with your actual API key
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()
