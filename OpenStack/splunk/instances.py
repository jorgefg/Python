#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("nova")

response = requests.get(URL + '/servers/detail?all_tenants=1', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id", "name", "status", "type", "zone", "bootable", "cg", "description", "encrypted", "multiattach", "host", "user_id", "tenant_id", "created_at", "updated_at"]]

for server in data['servers']:
    t.append([
        server['id'],
        server['name'],
        server['status'],
        server['volume_type'],
        server['availability_zone'],
        server['bootable'],
        server['consistencygroup_id'],
        server['description'],
        server['encrypted'],
        server['multiattach'],
        server['os-vol-host-attr:host'],
        server['user_id'],
        server['os-vol-tenant-attr:tenant_id'],
        server['created_at'],
        server['updated_at']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11};{12};{13};{14}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
