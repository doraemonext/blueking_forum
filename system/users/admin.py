# -*- coding: utf-8 -*-

from django.contrib import admin
from system.users.models import User


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
