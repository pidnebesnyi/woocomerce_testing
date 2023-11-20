from ssqaapitest.src.helpers.coupons_helper import CouponsHelper
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.helpers.orders_helper import OrdersHelper
import pdb
import pytest
from ssqaapitest.src.utilities.dbUtility import DBUtility
from ssqaapitest.src.utilities.genericUtilities import genarate_random_string, genarate_random_number
@pytest.mark.coupons(scope='module')

@pytest.mark.parametrize('discount_type', [
    pytest.param('percent', marks=pytest.mark.tcid37),
    pytest.param('fixed_cart', marks=pytest.mark.tcid38),
    pytest.param('fixed_product', marks=pytest.mark.tcid39)
    ]
)
def test_create_a_coupon(discount_type):

    # create a new coupon
    coupon_amount = str(genarate_random_number())
    coupon_info = CouponsHelper().create_coupon(amount=coupon_amount, discount_type=discount_type)
    coupon_id = coupon_info['id']

    # check for a coupon with API call
    rs_api = CouponsHelper().get_coupon(id=coupon_id)
    assert rs_api['discount_type'] == discount_type, f"Discont type doesn't match. \"" \
                                                     f"Expected: {discount_type},\nActual: {rs_api['discount_type']}"\
                                                     f"\nCoupon ID: {coupon_id}"
    assert coupon_id == rs_api['id'], f"Unable to find coupon with ID = {coupon_id}"

    # check DB for a coupon
    sql_code = f"SELECT * FROM local.wp_posts WHERE post_type = 'shop_coupon' AND ID  = {coupon_id};"
    rs_db = DBUtility().execute_select(sql=sql_code)
    assert rs_db, f"can't find DB note for {coupon_id} coupon ID"

@pytest.mark.tcid40
def test_create_a_coupon_negative():
    # create a new coupon
    coupon_amount = str(genarate_random_number())
    coupon_info = CouponsHelper().create_coupon(amount=coupon_amount, discount_type=genarate_random_string(), expected_status_code=400)
    assert coupon_info['message'] == 'Invalid parameter(s): discount_type', f"coupon creation failed with the wrong message:\n"\
                                                                            f"{coupon_info['message']}"
    assert coupon_info['code'] == 'rest_invalid_param', f"coupon creation failed with the wrong message:\n"\
                                                                            f"{coupon_info['code']}"

