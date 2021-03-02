from django.contrib import admin

# Register your models here.

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = ["id"]


admin.site.register(Product, ProductAdmin)
