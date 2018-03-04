#!/usr/bin/env python3
import requests
import os

APP_ID_NAME = 'DEFAULT'
APP_ID_KEY = 'APPID_' + APP_ID_NAME

try:
    # APP_ID = os.environ[APP_ID_KEY + 'BLOOP']
    APP_ID = os.environ[APP_ID_KEY]
    
except KeyError:
    print('You do not have the required environment variable(s).')
    print('Possible causes:')
    print('1. You forgot to activate the virtualenv:')
    print('2. You forgot to edit the `activate` script of your env with the APPID')
    exit(1)

CITY_NAME = 'Sydney'
# headers = {'X-API-TOKEN': 'your_token_here'}
PAYLOAD = {'q': CITY_NAME, 'APPID': APP_ID}
URL = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s'%(PAYLOAD['q'], PAYLOAD['APPID'])
resp = requests.post(URL, data=PAYLOAD)
print(resp.content)
