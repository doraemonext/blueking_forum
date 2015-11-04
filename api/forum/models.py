# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models

from system.users.models import User


class ForumManager(models.Manager):
    pass


class Forum(models.Model):
    parent = models.ForeignKey('self', verbose_name='上级论坛', blank=True, null=True)
    name = models.CharField('名称', max_length=50)
    description = models.TextField('描述')
    displayorder = models.IntegerField('显示顺序', default=0)
    threads = models.BigIntegerField('主题数量', default=0)
    posts = models.BigIntegerField('帖子数量', default=0)
    today_posts = models.BigIntegerField('今日发帖数量', default=0)
    yesterday_posts = models.BigIntegerField('昨日发帖数量', default=0)

    objects = ForumManager()

    class Meta:
        db_table = 'forum'
        verbose_name = '板块'
        verbose_name_plural = '板块'


class ThreadManager(models.Manager):
    pass


class Thread(models.Model):
    forum = models.ForeignKey(Forum, verbose_name='所属板块')
    author = models.ForeignKey(User, verbose_name='作者', related_name='author')
    subject = models.CharField('标题', max_length=255)
    read_perm = models.SmallIntegerField('阅读权限', default=0)
    dateline = models.DateTimeField('发表日期', auto_now_add=True)
    last_post = models.DateTimeField('最后发表日期', auto_now=True)
    last_poster = models.ForeignKey(User, verbose_name='最后发表人', related_name='last_poster')
    views = models.IntegerField('浏览次数', default=0)
    replies = models.IntegerField('回复次数', default=0)
    stick = models.BooleanField('是否置顶', default=False)
    highlight = models.BooleanField('是否高亮', default=False)
    digest = models.BooleanField('是否精华', default=False)
    recommend_add = models.IntegerField('支持人数', default=0)
    recommend_sub = models.IntegerField('反对人数', default=0)
    favtimes = models.IntegerField('主题收藏次数', default=0)

    objects = ThreadManager()

    class Meta:
        db_table = 'thread'
        verbose_name = '主题'
        verbose_name_plural = '主题'


class PostManager(models.Manager):
    pass


class Post(models.Model):
    forum = models.ForeignKey(Forum, verbose_name='所属板块')
    thread = models.ForeignKey(Thread, verbose_name='所属主题')
    first = models.BooleanField('是否是首贴', default=False)
    author = models.ForeignKey(User, verbose_name='作者')
    dateline = models.DateTimeField('发表时间', auto_now_add=True)
    message = models.TextField('消息内容')
    anonymous = models.BooleanField('是否匿名', default=False)

    objects = PostManager()

    class Meta:
        db_table = 'post'
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
