#!/usr/bin/env python

import json
import requests
import base64
import sys
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+sio_host+'/api/login', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)

token = bytes.decode(base64.b64encode (bytes(':'+json.loads(response.text), "utf-8")))

headers = {'Accept':'application/json', 'Content-Type':'application/json', 'Authorization':'Basic '+token+''}

response = requests.get('https://'+sio_host+'/api/types/Volume/instances', headers=headers, verify=False)

json_data = json.loads(response.text)

pprint(json_data)