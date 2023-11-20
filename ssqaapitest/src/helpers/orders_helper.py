import os
import pdb

from ssqaapitest.src.utilities.wooAPIUtility import WOOAPIUtility
import json
from ssqaapitest.src.dao.orders_dao import OrderDAO

class OrdersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WOOAPIUtility()

    def create_order(self, additional_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more info to payload, then update it
        if additional_args:
            assert isinstance(additional_args, dict), f'parameter additional_args should be dict, received {type(additional_args)}'
            payload.update(additional_args)

        rs_api = self.woo_helper.post('orders', paramaters=payload, expected_status_code=201)
        return rs_api

    def verify_order_is_created(self, order_json, expected_customer_id, expected_product_ids: list):
        orders_dao = OrderDAO()

        # verify response
        assert order_json, f'create order json is empty'
        assert order_json[
                   'customer_id'] == expected_customer_id , f'customer_id is not 0, which means that it is not a guest user,\nactual ID: {order_json["customer_id"]}'
        assert len(order_json['line_items']) == len(expected_product_ids), f"Expected only {len(expected_product_ids)} item in order, but found {len(order_json['line_items'])}"

        # verify DB
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)
        assert line_info, f'create order line item not found in DB, order ID: {order_id}'

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1
        # get list of products IDs in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]
        for product in expected_product_ids:
            assert product['product_id'] in api_product_ids, f'Created order does not have at least one expected product'

    def call_update_order(self, order_id, data):
        return self.woo_helper.put(endpoint=f'orders/{order_id}', data=data)

    def call_retrieve_an_order(self, order_id):
        return self.woo_helper.get(f'orders/{order_id}')

