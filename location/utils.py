from string import ascii_letters, digits
from random import choice


def generate_restaurant_code(zip_code):
    random_char = "".join([choice(ascii_letters + digits) for _ in range(3)])
    return "{}{}".format(zip_code, random_char.lower())
