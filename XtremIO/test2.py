import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
from pprint import pprint

from config import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get('https://'+xio_host+'/api/json/v2/types/volumes', auth=HTTPBasicAuth(xio_user, xio_pass), verify=False)

json_data = json.loads(response.text)

pprint(json_data)
