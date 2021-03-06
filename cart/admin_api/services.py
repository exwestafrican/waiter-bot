from cart.models import OrderStatus
from users.services import add_activity


def create_order_status(admin, name):
    OrderStatus.objects.create(name=name)
    add_activity(admin, "{} admin created new status {}".format(admin, name))
    return True
