from location.models import Restaurant
from location.utils import generate_restaurant_code
from users.services import add_activity


def create_restaurant(
    admin,
    name: str,
    owner: object,
    address: str,
    available_in: object,
    in_school: bool,
    *args,
    **kwargs,
):
    restaurant = Restaurant(
        name=name,
        owner=user,
        address=address,
        available_in=available_in,
        in_school=in_school,
    )
    location_zip = available_in.location_zip
    code = generate_restaurant_code(location_zip)
    restaurant.code
    restaurant.save()
    add_activity(admin, "{} created a new restaurant".format(admin))
