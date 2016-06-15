#!/usr/bin/python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from cinderclient.v2 import client

auth = v3.Password(
    auth_url='http://192.168.10.194:5000/v3',
    username='admin',
    user_domain_name='Default',
    project_name = 'admin',
    project_domain_name='Default',
    password='changeme'
)

sess = session.Session(auth=auth)

cinder = client.Client(session=sess,endpoint_type='publicURL')

cinder.volumes.list()