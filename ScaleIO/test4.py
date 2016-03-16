#!/usr/bin/env python3

import uuid
import json
import scaleio
import requests
from pprint import pprint

url = 'http://192.168.10.184:9200'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

for volume in scaleio.get_volumes():
    data = (json.dumps(scaleio.get_volume(volume['id']),sort_keys=True,indent=4))
    r = requests.post(url+'/scaleio/volumes/'+str(uuid.uuid4()), data=data, headers=headers)
    pprint(r.text)
