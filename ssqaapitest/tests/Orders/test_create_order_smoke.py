
import pytest
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.dao.orders_dao import OrderDAO
from ssqaapitest.src.helpers.orders_helper import OrdersHelper
from ssqaapitest.src.helpers.customers_helper import CustomerHelper

@pytest.fixture(scope='module')
def my_orders_smoke_setup():
    rand_product = ProductsDAO().get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    order_helper = OrdersHelper()
    info = {'product_id': product_id,
            'order_helper': order_helper}
    return info

@pytest.mark.orders
@pytest.mark.smoke
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):


    customer_id = 0
    product_id = my_orders_smoke_setup['product_id']
    order_helper = my_orders_smoke_setup['order_helper']

    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)
    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json=order_json, expected_customer_id=customer_id, expected_product_ids=expected_products)

@pytest.mark.orders
@pytest.mark.smoke
@pytest.mark.tcid49
def test_create_order_new_created_customer(my_orders_smoke_setup):

    customer_helper = CustomerHelper()
    product_id = my_orders_smoke_setup['product_id']
    order_helper = my_orders_smoke_setup['order_helper']

    # make the call
    cust_info = customer_helper.create_customer()
    cust_id = cust_info['id']
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
            "customer_id": cust_id
    }
    order_json = order_helper.create_order(additional_args=info)
    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json=order_json, expected_customer_id=cust_id, expected_product_ids=expected_products)