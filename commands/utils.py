import re

SPECIAL_CHARACTERS = "[\s\-:;]"


def clean_data_set(*data_set):
    return [d.strip().lower() for data in data_set]


def clean_data(data):
    return data.strip().lower()


def clean_number(number):
    return number.replace(",", "")


def remove_word(msg, word):
    _msg = msg.replace(word, "")
    return clean_data(_msg)


def get_food_item(msg):
    regex = r"\w+{}*\d+".format(SPECIAL_CHARACTERS)
    match = re.findall(regex, msg)
    return match


def find_vendor_code(msg):
    regex_1 = r"vendor_code{}*\d+".format(SPECIAL_CHARACTERS)
    regex_2 = r"vendor code{}*\d+".format(SPECIAL_CHARACTERS)

    match = re.findall(regex_1, msg) + re.findall(regex_2, msg)
    if match:
        truncated_match = match[0].replace(" ", "")
        code = truncated_match[-3:]
        return {
            "success": True,
            "message": "",
            "data": {"code": code, "match": match[0]},
        }
    else:
        return {
            "success": False,
            "message": "You either forgot to enter a vendor code or misspelt. to get a list of vendor and code send #get_vendor_code",
            "data": {"code": ""},
        }


def item_in_list(list_item: list):
    if len(list_item) > 1:
        return True
    return False


def create_order_summary(items: list):
    regex = r"[\-:;]{1}"
    valid_inputs = []
    invalid_inputs = []
    valid_inputs_msg = []
    for item in items:
        item = clean_data(item)

        delimiter = re.findall(regex, item)[0]

        if delimiter is None or delimiter == "":
            invalid_inputs.append(
                "{}: please use a valid delimiter like - or , or : example. produce - amount".format(
                    item
                )
            )
            continue

        else:
            product, amount = item.split(delimiter)
            print(product, amount)
            try:
                int(amount)
                valid_inputs_msg.append(
                    "buy {} amount worth {}".format(product, amount)
                )
                valid_inputs.append({"product": product, "amount": int(amount)})
            except ValueError:
                invalid_inputs.append(
                    "{}: please ensure you use this format, produce - amount".format(
                        item
                    )
                )

    if item_in_list(invalid_inputs):
        return {"success": False, "message": ", ".join(invalid_inputs), "data": {}}

    elif item_in_list(valid_inputs):
        return {
            "success": True,
            "message": "please confrim your order summary {} and send #confirm_order to finalize your order".format(
                ", ".join(valid_inputs_msg)
            ),
            "data": valid_inputs,
        }
    else:
        return {
            "success": False,
            "message": "we couldn't figure out what you did wrong. please use #example_<command> to see how to use a command e.g example_make_order",
            "data": "",
        }


def initiate_order_request(msg, command):
    # check for restaurant short code
    refined_message = remove_word(msg, command)
    vendor_search = find_vendor_code(msg)
    validate_code = False
    code = vendor_search["data"]["code"]
    # if vendor search and in valid code
    if vendor_search.get("success") and validate_code is True:
        search_context = vendor_search["data"]["match"]
        # remove vendoer
        just_items_left = remove_word(refined_message, search_context)
        # send order summary
        items = get_food_item(just_items_left)

        summary = create_order_summary(items)
        return summary.get("message")
        # search for order item
    elif vendor_search.get("success") and validate_code is False:
        return "You didn't enter a valid vendor code, vendor code {} doesn't seem to belong to anyone".format(
            code
        )
    else:
        return "You didn't provide us a vendor code please go over the command example"
