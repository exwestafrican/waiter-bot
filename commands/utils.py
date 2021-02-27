import re


def clean_data_set(*data_set):
    return [d.strip().lower() for data in data_set]


def clean_data(data):
    return data.strip().lower()


def remove_word(msg, word):
    _msg = msg.replace(word, "")
    return clean_data(_msg)


def get_food_item(msg, command):
    return remove_word(msg, command)


def find_vendor_code(msg):
    SPECIAL_CHARACTERS = "[\s\-:;]"
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


def make_order(msg, command):
    # check for restaurant short code
    refined_message = remove_word(msg, command)
    vendor_search = find_vendor_code(msg)

    if vendor_search.get("success"):
        code = vendor_search["data"]["code"]
        search_context = vendor_search["data"]["match"]
        # remove vendoer
        remove_word(refined_message, search_context)
        return code
        # search for order item
    else:
        return "None"
