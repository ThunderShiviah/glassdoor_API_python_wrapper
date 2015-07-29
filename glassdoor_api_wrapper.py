# TODO: write a wrapper that checks if running with python 2 and exits.

import json
import urllib.request as request # urllib.requests requires python3.
import requests
import private_config as config # Change to config.

""" A small wrapper for Glassdoor's API. See http://stackoverflow.com/questions/30956891/rest-glassdoor-api-requires-user-agent-in-header for some useful info.

Make sure you fill in your Glassdoor API credentials in the config.py file."""

PARTNER_ID = config.partnerID
KEY = config.key
USERAGENT = "Mozilla/5.0"
MY_IP = json.loads(request.urlopen("http://ip.jsontest.com/").read().decode('utf-8'))['ip'] # From the stackoverflow answer
url = 'http://api.glassdoor.com/api/api.htm' 

payload = {'v':'1',
            'format':'json',
            't.p':PARTNER_ID,
            't.k':KEY,
            'userip':MY_IP,
            'useragent': USERAGENT,
            'action':'jobs-stats',
            'returnJobTitles':'true',
            'returnStates':'true'}

if __name__ == '__main__': 
    r = requests.get(url, 
            params=payload,
            headers =  {'User-Agent': USERAGENT}
            )
    print(r.status_code)
    print(r.headers)
