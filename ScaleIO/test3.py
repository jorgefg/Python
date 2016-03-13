#!/usr/bin/env python3

import scaleio
import json

volumes = []
for volume in scaleio.get_volumes():
    volumes.append(scaleio.get_volume(volume['id']))

print (json.dumps(volumes,sort_keys=True,indent=2))