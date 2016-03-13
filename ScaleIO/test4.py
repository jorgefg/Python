#!/usr/bin/env python3

import scaleio
import requests
from pprint import pprint

url = 'http://kibana.akinosoft.int:9200'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

for volume in scaleio.get_volumes():
    data = scaleio.get_volume(volume['id'])
    r = requests.post(url+'/'+volume['id'], data=data, headers=headers)
    pprint(r.text)
