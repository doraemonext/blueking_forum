# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    nickname = models.CharField(_('nickname'), max_length=30, default='')

    class Meta:
        db_table = 'user'
        default_permissions = ('add', 'change', 'delete', 'view')
