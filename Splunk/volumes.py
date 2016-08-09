#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("cinderv2")

response = requests.get(URL + '/volumes/detail?all_tenants=1', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id", "name", "size", "status", "type", "zone", "bootable", "cg", "description", "encrypted", "multiattach", "host", "user_id", "tenant_id", "created_at", "updated_at"]]

for volume in data['volumes']:
    t.append([
        volume['id'],
        volume['name'],
        volume['size'],
        volume['status'],
        volume['volume_type'],
        volume['availability_zone'],
        volume['bootable'],
        volume['consistencygroup_id'],
        volume['description'],
        volume['encrypted'],
        volume['multiattach'],
        volume['os-vol-host-attr:host'],
        volume['user_id'],
        volume['os-vol-tenant-attr:tenant_id'],
        volume['created_at'],
        volume['updated_at']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11};{12};{13};{14};{15}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15]))
