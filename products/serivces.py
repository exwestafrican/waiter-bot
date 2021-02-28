from products.models import Product
from decimal import Decimal


def create_product(
    admin: object,
    name: str,
    base_charge: Decimal,
    addition_charge: Decimal,
    measured_in: int,
    available: bool,
    countable: bool,
    sold_by: object,
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