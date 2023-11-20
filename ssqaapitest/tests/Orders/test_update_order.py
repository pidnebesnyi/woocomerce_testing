from ssqaapitest.src.helpers.orders_helper import OrdersHelper
import pdb
import pytest
from ssqaapitest.src.utilities.wooAPIUtility import WOOAPIUtility
from ssqaapitest.src.utilities.genericUtilities import genarate_random_string

@pytest.mark.orders(scope='module')

# @pytest.mark.tcid55
# @pytest.mark.orders
@pytest.mark.parametrize('new_status', [
    pytest.param('cancelled', marks=pytest.mark.tcid55),
    pytest.param('completed', marks=pytest.mark.tcid56),
    pytest.param('on-hold', marks=pytest.mark.tcid57),
    ]
)
def test_update_order_status(new_status):

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()

    # get the current status
    current_status = order_json['status']
    assert current_status != new_status, f'Current status of order is already {current_status}, unable to run case'

    # update the status
    order_id = order_json['id']
    payload = {'status': new_status}
    call_update_order = order_helper.call_update_order(order_id=order_id, data=payload)
    updated_status = call_update_order['status']

    # verify the new status
    assert updated_status == new_status, f'The status didnt change.\nExpected results: {new_status}\nActual Result: {updated_status}'

    # get order info
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    updated_status = new_order_info['status']
    # verify the new status
    assert updated_status == new_status, f'The status didnt change.\nExpected results: {new_status}\nActual Result: {updated_status}'

@pytest.mark.regression
@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    new_status = 'abcde'
    woo_helper = WOOAPIUtility()
    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']



    # update the status
    payload = {'status': new_status}
    call_update_order = woo_helper.put(endpoint=f'orders/{order_id}', data=payload, expected_status_code=400)
    assert call_update_order['code'] == 'rest_invalid_param', f"call_update_order failed with an unexpected failure: {call_update_order['code']}"
    assert call_update_order['message'] == "Invalid parameter(s): status", f"call_update_order failed with an unexpected message: {call_update_order['message']}"


@pytest.mark.tcid59
def test_update_order_customer_note():

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']
    rand_customer_note = genarate_random_string(40)
    payload = {'customer_note': rand_customer_note}
    order_helper.call_update_order(order_id=order_id, data=payload)
    customer_note = order_helper.call_retrieve_an_order(order_id)
    assert customer_note['customer_note'] == rand_customer_note, f"Expected: {rand_customer_note}.\nActual: {customer_note['customer_note']}"
