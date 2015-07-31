#!/usr/bin/env python

# List ViPR volumes and their capacity

from vipr import *

client = ViPR(
        username='root',
        password='ChangeMe1!',
        token_endpoint='https://192.168.10.182:4443/login',
        vipr_endpoint='https://192.168.10.182:4443',
        request_timeout=30,
        verify_ssl=False
    )

volume_list = client.blockvolume.get_volumes_bulk()
volume_count = 0
volume_capacity = 0
for volume_id in volume_list:
    volume_info = client.blockvolume.get_volume(volume_id)
    if (volume_info['inactive'] == False):
        capacity = int(float(volume_info['provisioned_capacity_gb']))
        print (volume_info['name']),(capacity)
        volume_count += 1
        volume_capacity += capacity
print ("Total volumes: %s" % volume_count)
print ("Total capacity: %s" % volume_capacity)