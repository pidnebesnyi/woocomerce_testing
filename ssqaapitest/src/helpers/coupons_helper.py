"""Helper class to work with coupons"""

from ssqaapitest.src.utilities.genericUtilities import genarate_random_string
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


class CouponsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_coupon(self, code=None, discount_type="percent", amount='50', individual_use=True,
                      exclude_sale_items=True, minimum_amount='1', expected_status_code=201, **kwargs):
        if not code:
            code = genarate_random_string()
        payload = dict()

        payload['code'] = code
        payload['discount_type'] = discount_type
        payload['amount'] = amount
        payload['individual_use'] = individual_use
        payload['exclude_sale_items'] = exclude_sale_items
        payload['minimum_amount'] = minimum_amount
        payload.update(kwargs)
        create_coupon = self.requests_utility.post('coupons', payload=payload, expected_status_code=expected_status_code)

        return create_coupon

    def get_coupon(self, id):
        if not id:
            raise Exception('No ID provided')

        get_coupon = self.requests_utility.post(f'coupons/{id}')
        return get_coupon
