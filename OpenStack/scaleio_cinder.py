import json
import requests
import base64
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from keystoneauth1.identity import v3
from keystoneauth1 import session
from cinderclient.v2 import client
from prettytable import PrettyTable
import os
import uuid

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sio_host = '192.168.10.194'
sio_user = 'user'
sio_pass = 'ScaleIO#2016
sio_port = '8443'

def scaleio_get_volumes():
    response = requests.get('https://'+sio_host+':'+sio_port+'/api/types/Volume/instances', headers=headers, verify=False)
    return response.json()

def get_volume_id(cinder, volume):
    formatted_volume = str(volume)
    splitted_string = formatted_volume.split()
    id = splitted_string[1].strip('>')
    return id

auth = v3.Password(
    auth_url=os.getenv('OS_AUTH_URL'),
    username=os.getenv('OS_USERNAME'),
    user_domain_name=os.getenv('OS_USER_DOMAIN_NAME','default'),
    project_name = os.getenv('OS_PROJECT_NAME'),
    project_domain_name=os.getenv('OS_PROJECT_DOMAIN_NAME','default'),
    password=os.getenv('OS_PASSWORD')
)

sess = session.Session(auth=auth,verify=False)

cinder = client.Client(session=sess,endpoint_type='publicURL')

response = requests.get('https://'+sio_host+':'+sio_port+'/api/login', auth=HTTPBasicAuth(sio_user, sio_pass), verify=False)
token = bytes.decode(base64.b64encode (':'+json.loads(response.text)))
headers = {'Content-Type':'application/json', 'Authorization':'Basic '+token+''}

data = scaleio_get_volumes()

t = PrettyTable(['ID', 'Name', 'ScaleIO Name', 'ScaleIO ID', 'Size'])

for volume in data:
    full_volume_sio_name = volume['name']
    full_volume_sio_id = volume['id']
    full_volume_sio_size = volume['sizeInKb'] / 1048576
    converted_name = base64.b16encode(base64.b64decode(volume['name']))
    converted_name_lower = converted_name.lower()
    os_id = uuid.UUID(converted_name_lower)
    try:
        full_volume_os_id = cinder.volumes.get(os_id)._info['id']
    except:
        full_volume_os_id = '(not found)'
    try:
        full_volume_os_name = cinder.volumes.get(os_id)._info['name']
    except:
        full_volume_os_name = ''
    try:
        full_volume_os_size = cinder.volumes.get(os_id)._info['size']
    except:
        full_volume_os_size = '0'
    t.add_row([full_volume_os_id, full_volume_os_name, full_volume_sio_name, full_volume_sio_id, full_volume_sio_size])

print t