# -*- coding: utf-8 -*-

from django.contrib import admin

from system.users.models import Group, MemberGroupPermission, SystemGroupPermission, User


class GroupAdmin(admin.ModelAdmin):
    pass


class MemberGroupPermissionAdmin(admin.ModelAdmin):
    pass


class SystemGroupPermissionAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(MemberGroupPermission, MemberGroupPermissionAdmin)
admin.site.register(SystemGroupPermission, SystemGroupPermissionAdmin)
admin.site.register(User, UserAdmin)
