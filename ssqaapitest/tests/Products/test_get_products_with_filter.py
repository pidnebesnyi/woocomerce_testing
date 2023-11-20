
import pytest
from _datetime import datetime,timedelta
from ssqaapitest.src.helpers.products_helper import ProductsHelper
import pdb
from ssqaapitest.src.dao.products_dao import ProductsDAO

@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_get_products_with_filter(self):

        # create data
        x_days_from_today = 300
        _after_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_date = _after_date.isoformat()
        payload = dict()
        payload['after'] = after_date

        # make a call
        rs_api = ProductsHelper().call_list_products(payload=payload)
        assert rs_api, 'Empty response'

        # get data from DB
        db_data = ProductsDAO().get_product_created_after_given_date(_date=after_date)

        # verify the response
        assert len(rs_api) == len(db_data), f'Assertion Failed\nResponse len = {len(rs_api)}\nDB len = {len(db_data)}'

        ids_in_api = [i['id']for i in rs_api]
        ids_in_db = [i['ID']for i in db_data]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f'List products with filter. Products response IDs doesnt match DB'