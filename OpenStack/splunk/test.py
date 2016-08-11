#!/usr/bin/env python

import requests
import json
import auth
import telemetry

URL, HEADERS = auth.plugin("nova")

a = telemetry.nova_plugin("fee49497-f699-4e91-b073-74bf758e3dec",HEADERS)

print(json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')))
