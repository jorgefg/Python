#!/usr/bin/env python

import xtremio

volume_list = blockvolume.get_volumes_bulk()
for volume_name in volume_list:
    print (volume_name)
