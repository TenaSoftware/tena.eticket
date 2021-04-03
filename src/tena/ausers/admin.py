from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UA

from ausers.models import Customer, Region, Woreda, Zone


@admin.register(get_user_model())
class UserAdmin(UA):
    pass

admin.site.register(Region)
admin.site.register(Zone)
admin.site.register(Woreda)
admin.site.register(Customer)
