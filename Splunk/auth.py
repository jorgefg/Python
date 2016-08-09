#!/usr/bin/env python

import requests
import json
from config import *

def plugin(service):

    headers = {"Content-type": "application/json"}

    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "domain": {
                            "name": OS_USER_DOMAIN_NAME
                        },
                        "name": OS_USERNAME,
                        "password": OS_PASSWORD
                    }
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": OS_PROJECT_DOMAIN_NAME
                    },
                    "name": OS_PROJECT_NAME
                }
            }
        }
    }

    response = requests.post(OS_AUTH_URL + '/auth/tokens', data=json.dumps(data), headers=headers, verify=False)

    TOKEN = response.headers['X-Subject-Token']

    keystone = json.loads(response.text)

    for catalog in keystone['token']['catalog']:
        if catalog['name']==service:
            for endpoint in catalog['endpoints']:
                if endpoint['interface']=="public":
                    URL=endpoint['url']

    HEADERS = {
        "Content-type": "application/json",
        "X-Auth-Token": TOKEN
    }

    return URL,HEADERS