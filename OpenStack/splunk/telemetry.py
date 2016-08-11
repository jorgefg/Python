#!/usr/bin/env python

import requests
import json
from config import *

def getvalue(resource_id,meter,headers):

    oldheaders = headers

    headers.update({"X-Subject-Token": headers['X-Auth-Token']})

    response = requests.get(OS_AUTH_URL + '/auth/tokens', headers=headers, verify=False)

    keystone = json.loads(response.text)

    for catalog in keystone['token']['catalog']:
        if catalog['name']=="ceilometer":
            for endpoint in catalog['endpoints']:
                if endpoint['interface']=="public":
                    URL=endpoint['url']

    data = "{\"filter\": \"{\\\"and\\\":[{\\\"=\\\":{\\\"resource_id\\\":\\\""+resource_id+"\\\"}},{\\\"=\\\":{\\\"meter\\\":\\\""+meter+"\\\"}}]}\", \"orderby\" : \"[{\\\"timestamp\\\": \\\"DESC\\\"}]\", \"limit\": \"1\"}"

    response = requests.post(URL + '/v2/query/samples', data=data, headers=oldheaders, verify=False)

    if response.text=="[]":
        ret = ""
    else:
        for line in json.loads(response.text):
            ret = line['volume']

    return ret

def nova_plugin(resource_id,headers):

    data = {}

    data["vcpus"] = getvalue(resource_id, "vcpus", headers)
    data["compute.instance.booting.time"] = getvalue(resource_id, "compute.instance.booting.time", headers)
    data["cpu_util"] = getvalue(resource_id, "cpu_util", headers)
    data["disk.allocation"] = getvalue(resource_id, "disk.allocation", headers)
    data["disk.capacity"] = getvalue(resource_id, "disk.capacity", headers)
    data["disk.device.allocation"] = getvalue(resource_id, "disk.device.allocation", headers)
    data["disk.device.capacity"] = getvalue(resource_id, "disk.device.capacity", headers)
    data["disk.device.read.requests.rate"] = getvalue(resource_id, "disk.device.read.requests.rate", headers)
    data["disk.device.usage"] = getvalue(resource_id, "disk.device.usage", headers)
    data["disk.device.write.bytes.rate"] = getvalue(resource_id, "disk.device.write.bytes.rate", headers)
    data["disk.device.write.requests.rate"] = getvalue(resource_id, "disk.device.write.requests.rate", headers)
    data["disk.ephemeral.size"] = getvalue(resource_id, "disk.ephemeral.size", headers)
    data["disk.read.bytes.rate"] = getvalue(resource_id, "disk.read.bytes.rate", headers)
    data["disk.read.requests.rate"] = getvalue(resource_id, "disk.read.requests.rate", headers)
    data["disk.root.size"] = getvalue(resource_id, "disk.root.size", headers)
    data["disk.usage"] = getvalue(resource_id, "disk.usage", headers)
    data["disk.write.bytes.rate"] = getvalue(resource_id, "disk.write.bytes.rate", headers)
    data["disk.write.requests.rate"] = getvalue(resource_id, "disk.write.requests.rate", headers)
    data["image"] = getvalue(resource_id, "image", headers)
    data["image.size"] = getvalue(resource_id, "image.size", headers)
    data["instance"] = getvalue(resource_id, "instance", headers)
    data["ip.floating"] = getvalue(resource_id, "ip.floating", headers)
    data["memory"] = getvalue(resource_id, "memory", headers)
    data["memory.resident"] = getvalue(resource_id, "memory.resident", headers)
    data["memory.usage"] = getvalue(resource_id, "memory.usage", headers)
    data["network.incoming.bytes.rate"] = getvalue(resource_id, "network.incoming.bytes.rate", headers)
    data["network.incoming.packets.rate"] = getvalue(resource_id, "network.incoming.packets.rate", headers)
    data["network.outgoing.bytes.rate"] = getvalue(resource_id, "network.outgoing.bytes.rate", headers)
    data["network.outgoing.packets.rate"] = getvalue(resource_id, "network.outgoing.packets.rate", headers)
    data["volume.size"] = getvalue(resource_id, "volume.size", headers)

    return data
