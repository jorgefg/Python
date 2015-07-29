import os
import json
import requests
from api import *

requests.packages.urllib3.disable_warnings()

class print_json():

    def __init__(self, message):
        self.message = message
        print (json.dumps(self.message,sort_keys=True,indent=4, separators=(',', ': ')))

class Authentication():

    def __init__(self, connection):
        self.conn = connection

class TokenRequest(object):

    def __init__(self, username, password, vipr_endpoint, token_endpoint, verify_ssl, token_filename, token_location, request_timeout, cache_token):
        self.username = username
        self.password = password
        self.vipr_endpoint = vipr_endpoint
        self.token_endpoint = token_endpoint
        self.verify_ssl = verify_ssl
        self.token_verification_endpoint = vipr_endpoint + '/user/whoami'
        self.token_filename = token_filename
        self.token_location = token_location
        self.request_timeout = request_timeout
        self.cache_token = cache_token
        self.token_file = os.path.join(self.token_location, self.token_filename)
        self.session = requests.Session()

    def get_new_token(self):
        self.session.auth = (self.username, self.password)
        req = self.session.get(self.token_endpoint, verify=self.verify_ssl, headers={'Accept': 'application/json'}, timeout=self.request_timeout)
        token = req.headers['x-sds-auth-token']
        if self.cache_token:
            with open(self.token_file, 'w') as token_file:
                token_file.write(token)
        return token

    def get_token(self):
        token = self._get_existing_token()
        if token:
            return token
        return self.get_new_token()

    def _get_existing_token(self):
        if os.path.isfile(self.token_file):
            with open(self.token_file, 'r') as token_file:
                return token_file.read()
        return None

    def _request(self, token, url):
        headers = {'Accept': 'application/json', 'X-SDS-AUTH-TOKEN': token}
        self.session.get(url, verify=self.verify_ssl, headers=headers, timeout=self.request_timeout)

class ViPR(object):

    def __init__(self, username=None, password=None, token=None, vipr_endpoint=None, token_endpoint=None, verify_ssl=False, token_filename='viperpy.tkn', token_location='.', request_timeout=15.0, cache_token=True):
        self.username = username
        self.password = password
        self.token = token
        self.vipr_endpoint = vipr_endpoint.rstrip('/')
        self.token_endpoint = token_endpoint.rstrip('/')
        self.verify_ssl = verify_ssl
        self.token_filename = token_filename
        self.token_location = token_location
        self.request_timeout = request_timeout
        self.cache_token = cache_token
        self._session = requests.Session()
        self._token_request = TokenRequest(username=self.username, password=self.password, vipr_endpoint=self.vipr_endpoint, token_endpoint=self.token_endpoint, verify_ssl=self.verify_ssl, token_filename=self.token_filename, token_location=self.token_location, request_timeout=self.request_timeout, cache_token=self.cache_token)
        self.token_file = os.path.join(self.token_location, self.token_filename)
        # API -> Authentication
        self.authentication = Authentication(self)
        # API -> Block Services
        self.blockvolume = BlockVolume(self)
        self.blocksnapshot = BlockSnapshot(self)

    def get_token(self):
        return self._token_request.get_new_token()

    def _fetch_headers(self):
        if self.token:
            return {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-sds-auth-token': self.token}
        else:
            return {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-sds-auth-token': self._token_request.get_token()}

    def _construct_url(self, url):
        return '{0}/{1}'.format(self.vipr_endpoint, url)

    def get(self, url, params=None):
        return self._request(url, params=params)

    def post(self, url, json_payload='{}'):
        return self._request(url, json_payload, http_verb='POST')

    def put(self, url, json_payload='{}'):
        return self._request(url, json_payload, http_verb='PUT')

    def _request(self, url, json_payload='{}', http_verb='GET', params=None):
        json_payload = json.dumps(json_payload)
        if http_verb == "PUT":
            req = self._session.put(self._construct_url(url), verify=self.verify_ssl, headers=self._fetch_headers(), timeout=self.request_timeout, data=json_payload)
        elif http_verb == 'POST':
            req = self._session.post(self._construct_url(url), verify=self.verify_ssl, headers=self._fetch_headers(), timeout=self.request_timeout, data=json_payload)
        else:
            req = self._session.get(self._construct_url(url), verify=self.verify_ssl, headers=self._fetch_headers(), timeout=self.request_timeout, params=params)
        return req.json()
