#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class BlockVolume():

    def __init__(self, connection):
        self.conn = connection

    def get_volumes_bulk(self):
        json_data = requests.get('https://'+xio_host+'/api/json/v2/types/volumes', auth=HTTPBasicAuth(xio_user, xio_pass), verify=False)
        return json_data['name']

    def get_volume(self, volume_id):
        return self.conn.get('block/volumes/{0}'.format(volume_id))