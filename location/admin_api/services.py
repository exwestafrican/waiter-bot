from location.models import Restaurant
from location.utils import generate_restaurant_code
from users.services import add_activity


def create_restaurant(
    admin,
    name: str,
    owner: object,
    address: str,
    available_in: object,
    in_school: bool = True,
):
    prefix = name[0]
    restaurant = Restaurant.objects.create(
        name=name,
        owner=owner,
        address=address,
        in_school=in_school,
        code=generate_restaurant_code(prefix),
    )
    for location in available_in:
        restaurant.available_in.add(location)

    add_activity(admin, "{} created a new restaurant".format(admin))
