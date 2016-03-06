#!/usr/bin/env python3

import json
import requests
import base64
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+sio_host+'/api/login', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)
token = bytes.decode(base64.b64encode (bytes(':'+json.loads(response.text), "utf-8")))
headers = {'Content-Type':'application/json', 'Authorization':'Basic '+token+''}

response = requests.get('https://'+sio_host+'/api/types/Volume/instances', headers=headers, verify=False)
data = response.json()
for volume in data:
    response = requests.get('https://'+sio_host+volume['links'][1]['href'], headers=headers, verify=False)
    statistics = response.json()
    print (
        volume['id'],
        volume['name'],
        volume['sizeInKb'],
        volume['volumeType'],
        volume['useRmcache'],
        statistics['userDataReadBwc']['totalWeightInKb'],
        statistics['userDataReadBwc']['numOccured'],
        statistics['userDataWriteBwc']['totalWeightInKb'],
        statistics['userDataWriteBwc']['numOccured']
    )
