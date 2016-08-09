#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("keystone")

response = requests.get(URL + '/domains', headers=HEADERS, verify=False)

t = [["id", "name", "description", "enabled"]]

data = json.loads(response.text)

for domain in data['domains']:
    t.append([
        domain['id'],
        domain['name'],
        domain['description'],
        domain['enabled']
    ])

for line in t:
    print("{0};{1};{2};{3}".format(line[0], line[1], line[2], line[3]))
