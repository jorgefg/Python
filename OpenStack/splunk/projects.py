#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("keystone")

response = requests.get(URL + '/projects', headers=HEADERS, verify=False)

t = [["id", "name", "description", "enabled", "domain_id", "parent_id"]]

data = json.loads(response.text)

for project in data['projects']:
    t.append([
        project['id'],
        project['name'],
        project['description'],
        project['enabled'],
        project['domain_id'],
        project['parent_id']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5}".format(line[0], line[1], line[2], line[3], line[4], line[5]))
