#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("ceilometer")

response = requests.get(URL + '/v2/samples', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id", "meter", "project_id", "recorded_at", "resource_id", "source", "timestamp", "type", "unit", "user_id", "volume"]]

for meter in data:
    t.append([
        meter['id'],
        meter['meter'],
        meter['project_id'],
        meter['recorded_at'],
        meter['resource_id'],
        meter['source'],
        meter['timestamp'],
        meter['type'],
        meter['unit'],
        meter['user_id'],
        meter['meter'],
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
