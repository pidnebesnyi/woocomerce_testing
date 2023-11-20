import pdb

import pytest
import logging as logger
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.dao.customers_dao import CustomersDAO
from ssqaapitest.src.utilities.wooAPIUtility import WOOAPIUtility


@pytest.mark.tcid29
@pytest.mark.customers
def test_create_customer_only_email_password():
    rand_info = generate_random_email_password()
    email = rand_info.get('email')
    password = rand_info.get('password')
    logger.info('TEST 29: Create a customer with email and password')

    # make the call
    logger.debug('cust_object = CustomerHelper()')
    cust_object = CustomerHelper()

    # verify status code of the codee
    cust_api_info = cust_object.create_customer(email=email, password=password)

    # verify email in the response
    assert cust_api_info['email'] == email, f'Create_customer API returned wrong email'
    assert cust_api_info['first_name'] == '', f'Create_customer API returned value for first name'

    # verify customer is created in database

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db, f'Create Customer response ID is not the same as ID in DB'

@pytest.mark.tcid47
@pytest.mark.customers
def test_create_customer_fail_for_existing_email():

    # get existing email from DB
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']
    request_helper = RequestsUtility()
    payload = {'email': existing_email, 'password': 'Password1'}
    cust_api_info = request_helper.post(endpoint='customers', payload=payload,expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f'Create Customer with existing user error code is not correct.\n expected: "registration-error-email-exists"\n actual: {cust_api_info["code"]}'


@pytest.mark.tcid1
@pytest.mark.test_smoke
def test_get_test():

    # get existing email from DB
    obj = WOOAPIUtility()
    rs_api = obj.get('products')