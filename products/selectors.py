def product_is_valid(product_name):
    return product.objects.filter(name=product_name).exists()


def valid_product_ordered(order_list):
    for product in order_list:
        pass

