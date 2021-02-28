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
    restaurant = Restaurant.objects.create(
        name=name,
        owner=owner,
        address=address,
        in_school=in_school,
    )
    for location in available_in:
        restaurant.available_in.add(location)
    prefix = name[0]
    code = generate_restaurant_code(prefix)
    restaurant.code = code
    restaurant.save()
    print("doing this", code)
    add_activity(admin, "{} created a new restaurant".format(admin))
