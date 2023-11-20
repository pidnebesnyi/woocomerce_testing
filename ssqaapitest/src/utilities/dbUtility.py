"""DB Utility to create a DB connection and execute SQL quarries"""


import pymysql
import logging as logger
from ssqaapitest.src.utilities.credentialsUtility import CredentialUtility
from ssqaapitest.src.configs.hosts_config import DB_HOSTS
import os


class DBUtility(object):

    def __init__(self):
        self.creds = CredentialUtility.get_dab_credentials()
        self.machine = os.environ.get('MACHINE')
        assert self.machine

        self.env = os.environ.get('ENV', 'test')
        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Can't start docker with local, use AMPS instead")

        self.host = DB_HOSTS[self.machine][self.env]
        self.socket = DB_HOSTS[self.machine][self.env]['socket']
        self.port = DB_HOSTS[self.machine][self.env]['port']
        self.database = DB_HOSTS[self.machine][self.env]['database']
        self.table_prefix = DB_HOSTS[self.machine][self.env]['table_prefix']

    def create_connection(self):
        if self.wp_host == 'local':

            connection = pymysql.connect(
                host=self.host,
                user=self.creds['db_user'],
                password=self.creds['dp_password'],
                unix_socket=self.socket
            )
        elif self.wp_host == 'ampps':
            connection = pymysql.connect(
                host=self.host,
                user=self.creds['db_user'],
                password=self.creds['dp_password'],
                port=self.port
            )
        else:
            raise Exception('Unknown WP_HOST')

        return connection

    def execute_select(self, sql):
        connection = self.create_connection()
        try:
            logger.debug(f'Executing SQL: {sql}')
            cur = connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()

        except Exception as e:
            raise Exception(f'Failed running sql: \n{sql}\nError: {str(e)}')
        finally:
            connection.close()

        return rs_dict

    def execute_sql(self, sql):
       pass
