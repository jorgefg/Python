#!/usr/bin/python

import uuid
import json
import scaleio
import requests
import time
from pprint import pprint

url = 'http://192.168.10.184:9200'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

json_data = {}
for volume in scaleio.get_volumes():
    json_data[volume['id']] = volume
    json_data[volume['id']]['date'] = int(time.time())

r = requests.post(url+'/scaleio/volumes', data=json_data, headers=headers)
pprint(r.text)