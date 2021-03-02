from django.contrib import admin

# Register your models here.
from cart.models import *


class CartAdmin(admin.ModelAdmin):
    model = Cart
    readonly_fields = ["id"]


admin.site.register(Cart, CartAdmin)
