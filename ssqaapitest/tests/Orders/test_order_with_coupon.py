from ssqaapitest.src.helpers.coupons_helper import CouponsHelper
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.helpers.orders_helper import OrdersHelper
import pdb
import pytest
from ssqaapitest.src.utilities.wooAPIUtility import WOOAPIUtility
from ssqaapitest.src.utilities.genericUtilities import genarate_random_string


@pytest.mark.tcid60
def test_update_order_with_coupon():
    # create a new coupon
    coupon_ammount = '50'
    coupon_info = CouponsHelper().create_coupon(amount=coupon_ammount)
    coupon_code = coupon_info['code']
    coupon_sale_amount = coupon_info['amount']

    # get a product
    new_product = ProductsHelper().call_create_product()
    product_id = new_product['id']
    regular_price = new_product['regular_price']
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "coupon_lines": [
            {
                "code": coupon_code
            }
        ]
    }
    # create an order with coupon
    order_json = OrdersHelper().create_order(additional_args=info)
    discount_total = order_json['discount_total']
    assert float(regular_price) * float(float(coupon_ammount)/100) == float(discount_total), f"Discount wasn't applied.\nRegular Price: {float(regular_price)},\ndiscount_total {discount_total}"
