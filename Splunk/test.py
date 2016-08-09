#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("cinderv2")

response = requests.get(URL + '/volumes/detail?all_tenants=1', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id", "name", "size"]]

for volume in data['volumes']:
    t.append([volume['id'], volume['name'], volume['size']])

for line in t:
    print("{0};{1};{2}".format(line[0], line[1], line[2]))
