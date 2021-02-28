from cart.models import OrderStatus


def get_order_status(**args):
    return OrderStatus.objects.filter(**args).first()


def get_quantity_ordered(product, amount_paid):
    base_charge = product.base_charge
    add_on_charge = product.addition_charge
    additional_amount_paid = subtract(amount_paid, base_charge)
    addition_units_ordered = float(additional_amount_paid) / float(add_on_charge)
    quantity_ordred = add(1, addition_units_ordered)


def validate_quantity_ordered(product, amount_paid):
    quantity_ordred = get_quantity_ordered(product, amount_paid)
    if whole_number(quantity_ordred):
        return True
    else:
        return False