#!/usr/bin/env python

# List ViPR volumes and their snapshots

from vipr import *

client = ViPR(
        username='root',
        password='ChangeMe1!',
        token_endpoint='https://192.168.10.182:4443/login',
        vipr_endpoint='https://192.168.10.182:4443',
        request_timeout=30
    )

snapshot_list = client.blocksnapshot.get_snapshots_bulk()
for snapshot_id in snapshot_list:
    snapshot_info = client.blocksnapshot.get_snapshot(snapshot_id)
    if (snapshot_info['inactive'] == False):
        volume_info = client.blockvolume.get_volume(snapshot_info['parent']['id'])
        print (volume_info['name']),(snapshot_info['name'])
