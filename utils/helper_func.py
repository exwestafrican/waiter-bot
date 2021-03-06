SPECIAL_CHARACTERS = "[\s\-:;]"


def clean_data(data):
    return data.strip().lower()


def add(*nums):
    total = float(0)
    for num in nums:
        total += float(num)
    return total


def multiply(*nums):
    total = float(1)
    for num in nums:
        total *= float(num)
    return total


def subtract(*nums):
    total = float(0)
    for num in nums:
        total -= float(num)
    return total


def convert_to_kobo(amount):
    return amount * 1000
