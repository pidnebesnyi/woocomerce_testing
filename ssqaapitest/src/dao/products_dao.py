"""Products Data Access Object"""

from ssqaapitest.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):
        # create a query
        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' LIMIT 1000;"
        # send a query to a database
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(quantity))

    def get_product_by_id(self, id):
        # create a query
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {id};"
        # send a query to a database
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_product_created_after_given_date(self, _date):
        # create a query
        sql = f'SELECT * FROM local.wp_posts WHERE post_type = "product" AND post_date > "{_date}" LIMIT 10000;'
        # send a query to a database
        return self.db_helper.execute_select(sql)
