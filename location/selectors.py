from location.models import Store


def get_products_in_store(store):
    return store.product_set.all()
