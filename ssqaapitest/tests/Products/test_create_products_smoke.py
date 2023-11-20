from ssqaapitest.src.utilities.genericUtilities import genarate_random_string
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_one_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = genarate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10'

    # make the api call
    product_response = ProductsHelper().call_create_product(payload=payload)


    # verify the response is not empty
    assert product_response, f'Create Product API is empty,\npayload is {payload}'
    assert product_response['name'] == payload['name'], f"Create Product API has unexpecterd name,\npayload is {payload}\nactual name:  {product_response['name']}"

    # verify product in the db
    product_id = product_response['id']
    db_product = ProductsDAO().get_product_by_id(id=product_id)
    assert payload['name'] == db_product[0]['post_title'], f"Payload name doesn't match DB name:\nPayload name = {payload['name']},\nDB name = {db_product[0]['post_title']}"
