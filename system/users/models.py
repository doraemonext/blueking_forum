# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.utils import DatabaseError
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils import timezone

from system.exceptions import InvalidOperationError


class GroupManager(models.Manager):
    pass


class Group(models.Model):
    TYPE_SYSTEM = 0
    TYPE_MEMBER = 1
    TYPE = (
        (TYPE_SYSTEM, '系统用户组'),
        (TYPE_MEMBER, '正常用户组'),
    )

    name = models.CharField('用户组名称', max_length=255, unique=True)
    type = models.SmallIntegerField('用户组类型', choices=TYPE)
    stars = models.SmallIntegerField('星星数', default=0)

    objects = GroupManager()

    class Meta:
        db_table = 'groups'
        verbose_name = '用户组'
        verbose_name_plural = '用户组'


class MemberGroupPermissionManager(models.Manager):
    def get_permission(self, group, names):
        """
        获取指定用户组的权限
        :param group: 用户组 Group Instance
        :param names: 权限名称 list, exp: ['read_access', 'max_attach_size']
        :return: 权限值 list, exp: [True, 2048]
        """
        queryset = self.filter(group=group)
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


class MemberGroupPermission(models.Model):
    group = models.OneToOneField(Group, verbose_name='所属用户组')
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

    objects = MemberGroupPermissionManager()

    class Meta:
        db_table = 'member_group_permissions'
        verbose_name = '正常用户组权限'
        verbose_name_plural = '正常用户组权限'


class SystemGroupPermissionManager(models.Manager):
    def get_permission(self, group, names):
        """
        获取指定用户组的权限
        :param group: 用户组 Group Instance
        :param names: 权限名称 list, exp: ['access_cp', 'allow_edit_post']
        :return: 权限值 list, exp: [True, False]
        """
        queryset = self.filter(group=group)
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


class SystemGroupPermission(models.Model):
    group = models.OneToOneField(Group, verbose_name='所属系统用户组')
    access_cp = models.BooleanField('允许访问管理面板', default=False)
    allow_edit_post = models.BooleanField('允许编辑帖子', default=False)
    allow_stick_thread = models.BooleanField('允许置顶主题', default=False)
    allow_delete_post = models.BooleanField('允许删除帖子', default=False)
    allow_edit_user = models.BooleanField('允许编辑用户', default=False)
    allow_post_announce = models.BooleanField('允许发布站点公告', default=False)
    allow_view_log = models.BooleanField('允许查看管理日志', default=False)
    allow_edit_forum = models.BooleanField('允许编辑板块', default=False)

    objects = SystemGroupPermissionManager()

    class Meta:
        db_table = 'system_group_permissions'
        verbose_name = '系统用户组权限'
        verbose_name_plural = '系统用户组权限'


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


class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=30, default='')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '用户'


class UserGroupsManager(models.Manager):
    def create(self, user, group):
        queryset = self.filter(user=user)
        for item in queryset:
            if item.group.type == group.type:
                raise InvalidOperationError('Cannot add the same group type to one user.')
        return self.create(user=user, group=group)


class UserGroups(models.Model):
    user = models.ForeignKey(User, verbose_name='所属用户')
    group = models.ForeignKey(Group, verbose_name='所属用户组')

    objects = UserGroupsManager()

    class Meta:
        db_table = 'user_groups'
        verbose_name = '用户与用户组联接表'
        verbose_name_plural = '用户与用户组联接表'
