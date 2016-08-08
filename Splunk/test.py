#!/usr/bin/env python

import requests
import json

OS_AUTH_URL='http://192.168.10.194:5000/v3'
OS_USERNAME='demo'
OS_PROJECT_DOMAIN_NAME='default'
OS_PASSWORD='changeme'

headers = {"Content-type": "application/json"}

data = {
    "auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "name": OS_USERNAME,
                    "domain": {"id": OS_PROJECT_DOMAIN_NAME},
                    "password": OS_PASSWORD
                }
            }
        },
        "scope": {
            "domain": {
                "id": OS_PROJECT_DOMAIN_NAME
            }
        }
  }
}

print(json.dumps(data, indent=4, sort_keys=True))
print(json.dumps(headers, indent=4, sort_keys=True))

#response = requests.get(OS_AUTH_URL+'/auth/tokens', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)