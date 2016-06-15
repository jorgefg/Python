#!/usr/bin/python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from cinderclient.v2 import client
import base64
from prettytable import PrettyTable
import os

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

volumes = cinder.volumes.list()

t = PrettyTable(['OpenStack ID', 'OpenStack Name', 'ScaleIO Name', 'Size (GB)'])
for volume in volumes:
    volume_id = get_volume_id(cinder, volume)
    volume_name = cinder.volumes.get(volume_id)._info['name']
    volume_size = cinder.volumes.get(volume_id)._info['size']
    volume_sio = volume_id.replace("-", "")
    volume_sio = base64.b64encode(base64.b16decode(volume_sio.upper()))
    t.add_row([volume_id,volume_name,volume_sio,volume_size])
print t
