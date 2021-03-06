from products.models import Product
from decimal import Decimal
from users.services import add_activity


def create_product(
    admin: object,
    name: str,
    base_charge: Decimal,
    addition_charge: Decimal,
    measured_in: int,
    sold_by: object,
    available: bool = True,
    countable: bool = False,
):
    Product.objects.create(
        name=name,
        base_charge=base_charge,
        addition_charge=addition_charge,
        available=available,
        countable=countable,
        sold_by=sold_by,
    )
    add_activity(
        admin, "{}, added new product for {}".format(admin.first_name, sold_by)
    )
    return True


def change_status_of_product(product):
    product.available = not bool(product.available)
    return product.available
