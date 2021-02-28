from django.contrib import admin
from commands.models import Command

# Register your models here.
class CommandAdmin(admin.ModelAdmin):
    model = Command


admin.site.register(Command, CommandAdmin)