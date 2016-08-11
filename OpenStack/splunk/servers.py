#!/usr/bin/env python

import requests
import json
import auth
import telemetry

URL, HEADERS = auth.plugin("nova")

response = requests.get(URL + '/servers/detail?all_tenants=1', headers=HEADERS, verify=False)

data = json.loads(response.text)

t = [["id", "name", "status", "instance", "zone", "hypervisor", "flavor", "launched_at", "terminated_at", "updated_at", "user_id", "tenant_id", "compute.instance.booting.time", "cpu_util", "disk.allocation", "disk.capacity", "disk.device.allocation", "disk.device.capacity", "disk.device.read.requests.rate", "disk.device.usage", "disk.device.write.bytes.rate", "disk.device.write.requests.rate", "disk.ephemeral.size", "disk.read.bytes.rate", "disk.read.requests.rate", "disk.root.size", "disk.usage", "disk.write.bytes.rate", "disk.write.requests.rate", "image", "image.size", "instance", "ip.floating", "memory", "memory.resident", "memory.usage", "network.incoming.bytes.rate", "network.incoming.packets.rate", "network.outgoing.bytes.rate", "network.outgoing.packets.rate", "vcpus", "volume.size"]]

for server in data['servers']:
    performance = telemetry.nova_plugin(server['id'], HEADERS)
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
        server['tenant_id'],
        performance['compute.instance.booting.time'],
        performance['cpu_util'],
        performance['disk.allocation'],
        performance['disk.capacity'],
        performance['disk.device.allocation'],
        performance['disk.device.capacity'],
        performance['disk.device.read.requests.rate'],
        performance['disk.device.usage'],
        performance['disk.device.write.bytes.rate'],
        performance['disk.device.write.requests.rate'],
        performance['disk.ephemeral.size'],
        performance['disk.read.bytes.rate'],
        performance['disk.read.requests.rate'],
        performance['disk.root.size'],
        performance['disk.usage'],
        performance['disk.write.bytes.rate'],
        performance['disk.write.requests.rate'],
        performance['image'],
        performance['image.size'],
        performance['instance'],
        performance['ip.floating'],
        performance['memory'],
        performance['memory.resident'],
        performance['memory.usage'],
        performance['network.incoming.bytes.rate'],
        performance['network.incoming.packets.rate'],
        performance['network.outgoing.bytes.rate'],
        performance['network.outgoing.packets.rate'],
        performance['vcpus'],
        performance['volume.size']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]))
