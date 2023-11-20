import logging as logger
import pdb
import pytest
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.utilities.genericUtilities import genarate_random_string, genarate_random_number

pytestmark = [pytest.mark.products, pytest.mark.smoke]


def create_product_helper():
    # create product
    payload = {'name': genarate_random_string(20),
               'type': 'simple',
               'regular_price': str(genarate_random_number())}
    return ProductsHelper().call_create_product(payload=payload)


@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get(endpoint='products')
    assert rs_api, f'Response of list API is empty'


@pytest.mark.tcid25
def test_get_product_by_id():
    # get a product from DB
    rand_product = ProductsDAO().get_random_product_from_db()
    rand_product_id = rand_product[0]['ID']

    # make a call
    response = ProductsHelper().get_product_by_id(id=rand_product_id)
    # verify a response
    assert rand_product[0]['post_title'] == response[
        'name'], f"Verification failed. \nDB name: rand_product[0]['post_title']\nAPI name: response['name']"


@pytest.mark.tcid61
def test_update_product_price():
    # create a product
    product_response = create_product_helper()
    product_id = product_response['id']
    old_price = product_response['regular_price']

    # change a price
    new_price_value = str(genarate_random_number())
    new_price_data = {
        "regular_price": new_price_value
    }
    ProductsHelper().call_update_product(product_id=product_id, payload=new_price_data)

    # get a product info again
    updated_product_info = ProductsHelper().get_product_by_id(id=product_id)
    new_price = updated_product_info['price']

    # verify the response
    assert old_price != new_price, f"Prices doesn't change!"
    assert new_price_value == new_price, f"Price provided by automation doesn't affect website. Expected result:{new_price_value}\nActual result: {new_price}"


@pytest.mark.tcid63
def test_update_product_price_check_on_sale_field():
    # create a product
    product_response = create_product_helper()

    # verify sale_price is not True
    assert not product_response['on_sale'], f'sale_price already has a value'

    # update sale_price
    regular_price = float(product_response['regular_price'])
    new_product_id = product_response['id']
    new_price_value = str(regular_price * 0.75)
    new_price_data = {
        "sale_price": new_price_value,
    }

    ProductsHelper().call_update_product(product_id=new_product_id, payload=new_price_data)

    # get a product info again
    updated_product_info = ProductsHelper().get_product_by_id(id=new_product_id)

    # verify the response
    updated_on_sale_value = updated_product_info['on_sale']
    assert updated_on_sale_value is True, f"on_sale value doesn't change after changing sale_price"

@pytest.mark.tcid64
def test_update_product_price_check_on_sale_field():
    # create a product
    product_response = create_product_helper()

    # verify sale_price is not True
    assert not product_response['on_sale'], f'sale_price already has a value'

    # update sale_price
    regular_price = float(product_response['regular_price'])
    new_product_id = product_response['id']
    new_price_value = str(regular_price * 0.75)
    new_price_data = {
        "sale_price": new_price_value,
    }

    ProductsHelper().call_update_product(product_id=new_product_id, payload=new_price_data)

    # get a product info again
    updated_product_info = ProductsHelper().get_product_by_id(id=new_product_id)

    # verify the response
    updated_on_sale_value = updated_product_info['on_sale']
    assert updated_on_sale_value is True, f"on_sale value doesn't change after changing sale_price"

    # update sale_price again with empty sale_price
    new_empty_price_data = {
        "sale_price": '',
    }
    ProductsHelper().call_update_product(product_id=new_product_id, payload=new_empty_price_data)

    # get a product info again
    updated_product_info = ProductsHelper().get_product_by_id(id=new_product_id)

    # verify the response
    updated_on_sale_value = updated_product_info['on_sale']
    logger.info(updated_on_sale_value)
    assert not updated_on_sale_value, f"on_sale value doesn't change after changing sale_price to an empty string"


@pytest.mark.tcid65
def test_update_product_sale_price_and_check():
    # create a product
    product_response = create_product_helper()

    # verify sale_price is not True

    # update sale_price
    regular_price = float(product_response['regular_price'])
    new_product_id = product_response['id']
    new_price_value = str(regular_price * 0.75)
    new_price_data = {
        "sale_price": new_price_value,
    }

    ProductsHelper().call_update_product(product_id=new_product_id, payload=new_price_data)

    # get a product info again
    updated_product_info = ProductsHelper().get_product_by_id(id=new_product_id)
    updated_new_price_value = updated_product_info["sale_price"]
    assert updated_new_price_value == new_price_value, f"sale_price field didn't change. \nExpected:{new_price_value}\nActual: {updated_new_price_value}"
