from django.contrib import admin

# Register your models here.
from location.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant


admin.site.register(Restaurant, RestaurantAdmin)
