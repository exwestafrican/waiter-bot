import re
from utils.helper_func import clean_data, SPECIAL_CHARACTERS


def get_food_item(msg):
    regex = r"\w+{}*\d+".format(SPECIAL_CHARACTERS)
    match = re.findall(regex, msg)
    return match


def get_product_price(item):
    regex = r"[\-:;]{1}"
    item = clean_data(item)
    delimiter = re.findall(regex, item)[0]
    if delimiter is None or delimiter == "":
        return {
            "success": False,
            "message": "{}: please use a valid delimiter like - or , or : example. produce - amount".format(
                item
            ),
        }
    else:
        product, amount = item.split(delimiter)
        return {"success": True, "data": {"price_amount": [product, amount]}}
