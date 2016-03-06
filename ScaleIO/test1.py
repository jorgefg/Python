#!/usr/bin/env python3

import scaleio
from pprint import pprint

data = scaleio.get_volumes()
for volume in data:
    statistics = scaleio.get_volume_statistics(volume['id'])
    pool = scaleio.get_pool(volume['storagePoolId'])
    info = scaleio.get_volume(volume['id'])
    mapped=False
    if info['mappedSdcInfo']:
        mapped=True
    thin=False
    print (
        volume['id'],
        volume['name'],
        volume['sizeInKb'],
        volume['volumeType'],
        volume['useRmcache'],
        volume['ancestorVolumeId'],
        pool['name'],
        mapped,
        statistics['userDataReadBwc']['totalWeightInKb'],
        statistics['userDataReadBwc']['numOccured'],
        statistics['userDataWriteBwc']['totalWeightInKb'],
        statistics['userDataWriteBwc']['numOccured']
    )
