# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from lib.utils import validator


class LoginSerializer(serializers.Serializer):
    """ 登录 API 接口 序列化类 """
    username = serializers.CharField(error_messages={'required': '用户名不能为空'}, validators=[
        validator.MinValue('用户名', 2),
        validator.MaxValue('用户名', 32),
        validator.SafeValue('用户名'),
    ])
    password = serializers.CharField(max_length=128, error_messages={'required': '密码不能为空'}, validators=[
        validator.MaxValue('密码', 64),
    ])
    next = serializers.CharField(max_length=255, required=False)


class RegisterSerializer(serializers.Serializer):
    """ 注册 API 接口 序列化类 """
    username = serializers.CharField(error_messages={'required': '用户名不能为空'}, validators=[
        validator.MinValue('用户名', 2),
        validator.MaxValue('用户名', 32),
        validator.SafeValue('用户名'),
    ])
    email = serializers.EmailField(error_messages={
        'required': '电子邮件不能为空',
        'invalid': '请输入合法的电子邮件地址',
    })
    password = serializers.CharField(max_length=128, error_messages={'required': '密码不能为空'}, validators=[
        validator.MaxValue('密码', 64),
    ])
    next = serializers.CharField(max_length=255, required=False)
