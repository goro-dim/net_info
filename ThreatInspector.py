# ThreatInspector.py

import requests

def query_abuseipdb(api_key, ip):
    # Mocked function to query AbuseIPDB
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90'
    headers = {
        'Key': 'YOUR_API_KEY',# Replace with your actual API key
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from AbuseIPDB'}
