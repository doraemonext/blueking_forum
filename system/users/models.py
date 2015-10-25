# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class GroupManager(models.Manager):
    pass


class Group(models.Model):
    name = models.CharField('用户组名称', max_length=255)
    stars = models.SmallIntegerField('星星数', default=0)

    objects = GroupManager()

    class Meta:
        db_table = 'groups'
        verbose_name = '用户组'
        verbose_name_plural = '用户组'


class PermissionManager(models.Manager):
    def get_permission(self, group, names):
        """
        获取指定用户组的权限
        :param group: 用户组 Group Instance
        :param names: 权限名称 list, exp: ['read_access', 'max_attach_size']
        :return: 权限值 list, exp: [True, 2048]
        """
        queryset = super(PermissionManager, self).filter(group=group)
        result = []
        if queryset.exists():
            perm = queryset[0]
            for name in names:
                if hasattr(perm, name):
                    result.append(getattr(perm, name))
                else:
                    raise ValueError('Permission name does not exist.')
            return result
        else:
            raise ValueError('Group does not exist.')


class Permission(models.Model):
    group = models.ForeignKey(Group, verbose_name='所属用户组')
    read_access = models.SmallIntegerField('阅读权限', default=0)
    allow_post = models.BooleanField('允许发帖', default=False)
    allow_reply = models.BooleanField('允许回复', default=False)
    allow_get_attach = models.BooleanField('允许下载/查看附件', default=False)
    allow_post_attach = models.BooleanField('允许发布附件', default=False)
    allow_post_image = models.BooleanField('允许发布图片', default=False)
    allow_search = models.BooleanField('允许搜索', default=False)
    allow_anonymous = models.BooleanField('允许匿名发帖', default=False)
    max_signature_size = models.IntegerField('用户签名最大字节数', default=0)
    max_attach_size = models.BigIntegerField('最大附件尺寸', default=0)
    attach_extensions = models.CharField('允许上传的附件扩展名', max_length=255, default='')

    objects = PermissionManager()

    class Meta:
        db_table = 'permissions'
        verbose_name = '权限'
        verbose_name_plural = '权限'


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
    username = models.CharField('用户名', max_length=30, unique=True)
    email = models.EmailField('电子邮件地址', max_length=255)
    group = models.ForeignKey(Group, verbose_name='所属用户组')
    nickname = models.CharField('昵称', max_length=30, default='')
    is_active = models.BooleanField('是否激活', default=False)
    date_joined = models.DateTimeField('注册日期', default=timezone.now)

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username
