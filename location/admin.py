from django.contrib import admin

# Register your models here.
from location.models import Store


class StoreAdmin(admin.ModelAdmin):
    model = Store


admin.site.register(Store, StoreAdmin)
