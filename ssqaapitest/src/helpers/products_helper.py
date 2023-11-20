import logging as logger
from ssqaapitest.src.utilities.genericUtilities import genarate_random_string, genarate_random_number
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_password
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger
from ssqaapitest.src.utilities.wooAPIUtility import WOOAPIUtility

class ProductsHelper(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.woo_api_utility = WOOAPIUtility()

    def get_product_by_id(self, id=1):
        return self.requests_utility.get(f'products/{id}')

    def call_create_product(self, payload=None):
        if not payload:
            # generate some data
            payload = dict()
            payload['name'] = genarate_random_string(20)
            payload['type'] = 'simple'
            payload['regular_price'] = str(genarate_random_number())

        return self.requests_utility.post(f'products', payload=payload, expected_status_code=201)

    def call_update_product(self, product_id, payload):
        return self.woo_api_utility.put(f'products/{product_id}', data=payload, expected_status_code=200)

    def call_list_products(self, payload=None):
        max_pages = 100000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f'List products page number {i}')

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add the current page number to the call
            payload['page'] = i
            rs_api = self.requests_utility.get(f'products', payload=payload)

            # if there is no response stop the loop
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception('Unable to find all the products after max_pages=100000')

        return all_products

