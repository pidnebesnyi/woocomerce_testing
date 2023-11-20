import json
import pdb

from ssqaapitest.src.configs.hosts_config import API_HOSTS
import requests
import os
from requests_oauthlib import OAuth1
import json
from ssqaapitest.src.utilities.credentialsUtility import CredentialUtility
import logging as logger

class RequestsUtility(object):

    def __init__(self):
        ws_creds = CredentialUtility.get_ws_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(ws_creds['ws_key'], ws_creds['ws_secret'],)

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Expected status code {self.expected_status_code}, but got {self.status_code} '

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}
        logger.info("HEY")
        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.response_json = rs_api.json()
        self.assert_status_code()
        logger.info(f'API POST Response: {self.response_json}')
        return self.response_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.response_json = rs_api.json()
        self.assert_status_code()
        logger.info(f'API GET Response: {self.response_json}')
        return self.response_json