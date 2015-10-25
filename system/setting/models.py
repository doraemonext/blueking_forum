# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class SettingManager(models.Manager):
    def create(self, name, value, force=False):
        """
        添加一条新的设置项
        :param name: 名称
        :param value: 内容
        :param force: 当force=True时, 如果添加的该设置项已经存在, 则强制更新
                      当force=False时, 如果添加的该设置项已经存在, 则不做任何操作
        :return: Setting实例
        """
        try:
            setting = super(SettingManager, self).get(name=name)
        except ObjectDoesNotExist:
            setting = super(SettingManager, self).create(name=name, value=value)
            return setting

        if force is True:
            setting.value = value
            setting.save()
        return setting

    def get(self, name):
        """
        根据name获取对应的选项内容
        :param name: 选项名称
        :return: 选项内容
        """
        return super(SettingManager, self).get(name=name).value

    def get_all(self):
        """
        获取所有的设置并以字典的形式返回
        :return: dict对象
        """
        settings = super(SettingManager, self).all()
        result = {}
        for item in settings:
            result[item.name] = item.value
        return result


class Setting(models.Model):
    name = models.CharField(u'选项名称', max_length=64, unique=True)
    value = models.TextField(u'选项内容')

    objects = SettingManager()

    class Meta:
        verbose_name = u'系统设置'
        verbose_name_plural = u'系统设置'
        db_table = 'setting'
