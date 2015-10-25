# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_superuser=False, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(u'用户名', max_length=30, unique=True)
    email = models.EmailField(u'电子邮件地址', max_length=255)
    nickname = models.CharField(u'昵称', max_length=30, default='')
    is_active = models.BooleanField(u'是否激活', default=False)
    date_joined = models.DateTimeField(u'注册日期', default=timezone.now)

    objects = UserManager()

    class Meta:
        db_table = 'user'
        default_permissions = ('add', 'change', 'delete', 'view')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username
