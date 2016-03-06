import json
import requests
import base64
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+sio_host+'/api/login', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)
token = bytes.decode(base64.b64encode (bytes(':'+json.loads(response.text), "utf-8")))
headers = {'Content-Type':'application/json', 'Authorization':'Basic '+token+''}

def get_volumes():
    response = requests.get('https://'+sio_host+'/api/types/Volume/instances', headers=headers, verify=False)
    return response.json()

def get_volume(id):
    response = requests.get('https://'+sio_host+'/api/instances/Volume::'+id, headers=headers, verify=False)
    return response.json()

def get_volume_statistics(id):
    response = requests.get('https://'+sio_host+'/api/instances/Volume::'+id+'/relationships/Statistics', headers=headers, verify=False)
    return response.json()

def get_pools():
    response = requests.get('https://'+sio_host+'/api/types/StoragePool/instances', headers=headers, verify=False)
    return response.json()

def get_pool(id):
    response = requests.get('https://'+sio_host+'/api/instances/StoragePool::'+id, headers=headers, verify=False)
    return response.json()
