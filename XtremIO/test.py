#!/usr/bin/env python

import xtremio
import json
from pprint import pprint

r = xtremio.get_volumes()
json_data = json.loads(r.text)
pprint(json_data)