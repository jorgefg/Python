import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
from pprint import pprint

from config import *
####
# A file named config.py must be created with the following content
# xio_host = 'ip or hostname'
# xio_user = 'username'
# xio_pass = 'password'
####

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+xio_host+'/api/json/v2/types/volumes', auth=HTTPBasicAuth(xio_user, xio_pass), verify=False)

json_data = json.loads(response.text)

pprint(json_data)


