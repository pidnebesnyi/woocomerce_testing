"""Module to get API and DB keys from environment"""

import os


class CredentialUtility(object):

    @staticmethod
    def get_ws_api_keys():
        ws_key = os.environ.get("WS_KEY")
        ws_secret = os.environ.get("WS_SECRET")

        if not ws_key or not ws_secret:
            raise Exception("No WS keys in the ENV")
        else:
            return {'ws_key': ws_key, 'ws_secret': ws_secret}

    @staticmethod
    def get_dab_credentials():
        db_user = os.environ.get("DB_USER")
        dp_password = os.environ.get("DB_PASSWORD")

        if not db_user or not dp_password:
            raise Exception("No DB keys in the ENV")
        else:
            return {'db_user': db_user, 'dp_password': dp_password}
