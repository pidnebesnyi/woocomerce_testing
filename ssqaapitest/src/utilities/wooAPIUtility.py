import json

from ssqaapitest.src.configs.hosts_config import WOO_API_HOSTS
import os
from ssqaapitest.src.utilities.credentialsUtility import CredentialUtility
from woocommerce import API
import logging as logger


class WOOAPIUtility(object):

    def __init__(self):
        ws_creds = CredentialUtility.get_ws_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]

        self.wcapi = API(
            url=self.base_url,
            consumer_key=ws_creds['ws_key'],
            consumer_secret=ws_creds['ws_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Expected status code {self.expected_status_code}, but got {self.status_code} '

    def get(self, endpoint, paramaters=None, expected_status_code=200):

        self.rs = self.wcapi.get(endpoint, params=paramaters)
        self.status_code = self.rs.status_code
        self.expected_status_code = expected_status_code
        self.response_json = self.rs.json()
        self.assert_status_code()
        return self.response_json

    def post(self, endpoint, paramaters=None, expected_status_code=200):

        self.rs = self.wcapi.post(endpoint, data=paramaters)
        self.status_code = self.rs.status_code
        self.expected_status_code = expected_status_code
        self.response_json = self.rs.json()
        self.assert_status_code()
        return self.response_json

    def put(self, endpoint, data=None, expected_status_code=200):

        self.rs = self.wcapi.put(endpoint=endpoint, data=data)
        self.status_code = self.rs.status_code
        self.expected_status_code = expected_status_code
        self.response_json = self.rs.json()
        self.assert_status_code()
        return self.response_json