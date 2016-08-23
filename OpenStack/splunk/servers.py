#!/usr/bin/env python

import requests
import json
import auth

URL, HEADERS = auth.plugin("nova")

response = requests.get(URL + '/servers/detail?all_tenants=1', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id",
      "name",
      "status",
      "instance",
      "zone",
      "hypervisor",
      "flavor",
      "launched_at",
      "terminated_at",
      "updated_at",
      "user_id",
      "tenant_id"
    ]]

for server in data['servers']:
    t.append([
        server['id'],
        server['name'],
        server['status'],
        server['OS-EXT-SRV-ATTR:instance_name'],
        server['OS-EXT-AZ:availability_zone'],
        server['OS-EXT-SRV-ATTR:hypervisor_hostname'],
        server['flavor']['id'],
        server['OS-SRV-USG:launched_at'],
        server['OS-SRV-USG:terminated_at'],
        server['updated'],
        server['user_id'],
        server['tenant_id']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11}".format(
        line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]
    ))
