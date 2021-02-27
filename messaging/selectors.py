from users.selectors import get_user


def get_name_or_number(number):
    user = get_user(phone_number=number)
    if user:
        return user.first_name
    else:
        return number