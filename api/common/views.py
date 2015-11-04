# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db import DatabaseError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, parsers

from api.common.serializer import LoginSerializer, RegisterSerializer
from system.users.models import User


class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (parsers.FormParser, )

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('ucenter:home')

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            redirect_url = serializer.data.get('next')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                response = {
                    'redirect_url': self.get_redirect_url(redirect_url),
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'non_field_errors': ['用户名或密码不正确'],
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (parsers.FormParser, )

    def get_redirect_url(self, next):
        if next:
            return next
        else:
            return reverse('ucenter:home')

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            redirect_url = serializer.data.get('redirect_url')

            try:
                User.objects.create_user(username=username, email=email, password=password)
            except DatabaseError:
                response = {
                    'non_field_errors': ['注册用户时出错，请联系管理员']
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            login(request, user)
            response = {
                'redirect_url': self.get_redirect_url(redirect_url)
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        logout(request)
        response = {
            'redirect_url': reverse('common:login'),
        }
        return Response(response, status=status.HTTP_200_OK)
