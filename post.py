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
print(APP_ID)
