#!/usr/bin/env python

import requests

OS_AUTH_URL='http://192.168.10.194:5000/v3'

class User(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username

data[auth][identity][methods]="password"
data[auth][identity][password]="password"

print data[auth]

#headers = '{'Content-type': 'application/json'}'

#response = requests.get(OS_AUTH_URL+'/auth/tokens', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)