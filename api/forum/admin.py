# -*- coding: utf-8 -*-

from django.contrib import admin

from api.forum.models import Forum, Thread, Post


class ForumAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)

