#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_volumes():
    return requests.get('https://'+xio_host+'/api/json/v2/types/volumes', auth=HTTPBasicAuth(xio_user, xio_pass), verify=False)

def get_volume_id(id):
    return requests.get('https://'+xio_host+'/api/json/v2/types/volumes/'+id, auth=HTTPBasicAuth(xio_user, xio_pass), verify=False)
