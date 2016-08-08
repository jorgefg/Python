#!/usr/bin/python

import json
import requests
import base64
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import *
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+sio_host+'/api/login', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)
#token = bytes.decode(base64.b64encode (bytes(':'+json.loads(response.text), "utf-8")))
token = bytes.decode(base64.b64encode (':'+json.loads(response.text)))
headers = {'Content-Type':'application/json', 'Authorization':'Basic '+token+''}

response = requests.get('https://'+sio_host+'/api/types/Volume/instances', headers=headers, verify=False)
data = response.json()

pprint (data)