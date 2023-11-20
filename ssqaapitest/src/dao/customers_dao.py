"""Customer Data Access Object"""

from ssqaapitest.src.utilities.dbUtility import DBUtility
import random


class CustomersDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):

        # create a query
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"

        # send a query to a database
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, quantity=1):
        sql = 'SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(quantity))
