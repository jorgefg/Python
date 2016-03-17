#!/usr/bin/env python3

import uuid
import json
import scaleio
import requests
import time
from pprint import pprint

url = 'http://192.168.10.184:9200'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

for volume in scaleio.get_volumes():
    data = json.loads(json.dumps(scaleio.get_volume(volume['id']), sort_keys=True, indent=2))
    data['date'] = int(time.time())
    data = json.dumps(data, sort_keys=True, indent=2)
    r = requests.post(url+'/scaleio/volumes/'+volume['id'], data=data, headers=headers)
    #r = requests.post(url+'/scaleio/volumes/'+str(uuid.uuid4()), data=data, headers=headers)
    pprint(r.text)
