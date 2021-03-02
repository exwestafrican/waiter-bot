from products.models import Product


def product_is_valid(product_name):
    return Product.objects.filter(name=product_name).exists()


def valid_product_ordered(order_list):
    for product in order_list:
        pass


def product_exists(**args):
    return Product.objects.filter(**args).exists()