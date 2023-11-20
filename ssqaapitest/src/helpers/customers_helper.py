import logging as logger

from ssqaapitest.src.utilities.genericUtilities import generate_random_email_password
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_password()
            email = ep['email']
        if not password:
            password = "Password1"
        payload = dict()

        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        create_customer = self.requests_utility.post('customers', payload=payload, expected_status_code=201)
        return create_customer