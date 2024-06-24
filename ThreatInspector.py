# ThreatInspector.py

import requests

def query_abuseipdb(api_key, ip):
    # Mocked function to query AbuseIPDB
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90'
    headers = {
        'Key': 'e4b32da34ddd7e8b84cdf76ee42f853696a92b4815742678e756100a092ba0d7a310e6b9a4d9907b',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from AbuseIPDB'}
