# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(default='', max_length=30, verbose_name='\u6635\u79f0')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u7528\u6237\u7ec4\u540d\u79f0')),
                ('type', models.SmallIntegerField(verbose_name='\u7528\u6237\u7ec4\u7c7b\u578b', choices=[(0, '\u7cfb\u7edf\u7528\u6237\u7ec4'), (1, '\u6b63\u5e38\u7528\u6237\u7ec4')])),
                ('stars', models.SmallIntegerField(default=0, verbose_name='\u661f\u661f\u6570')),
            ],
            options={
                'db_table': 'groups',
                'verbose_name': '\u7528\u6237\u7ec4',
                'verbose_name_plural': '\u7528\u6237\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='MemberGroupPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read_access', models.SmallIntegerField(default=0, verbose_name='\u9605\u8bfb\u6743\u9650')),
                ('allow_post', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e16')),
                ('allow_reply', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u56de\u590d')),
                ('allow_get_attach', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u4e0b\u8f7d/\u67e5\u770b\u9644\u4ef6')),
                ('allow_post_attach', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e03\u9644\u4ef6')),
                ('allow_post_image', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e03\u56fe\u7247')),
                ('allow_search', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u641c\u7d22')),
                ('allow_anonymous', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u533f\u540d\u53d1\u5e16')),
                ('max_signature_size', models.IntegerField(default=0, verbose_name='\u7528\u6237\u7b7e\u540d\u6700\u5927\u5b57\u8282\u6570')),
                ('max_attach_size', models.BigIntegerField(default=0, verbose_name='\u6700\u5927\u9644\u4ef6\u5c3a\u5bf8')),
                ('attach_extensions', models.CharField(default='', max_length=255, verbose_name='\u5141\u8bb8\u4e0a\u4f20\u7684\u9644\u4ef6\u6269\u5c55\u540d')),
                ('group', models.OneToOneField(verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4', to='users.Group')),
            ],
            options={
                'db_table': 'member_group_permissions',
                'verbose_name': '\u6b63\u5e38\u7528\u6237\u7ec4\u6743\u9650',
                'verbose_name_plural': '\u6b63\u5e38\u7528\u6237\u7ec4\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='SystemGroupPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_cp', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u8bbf\u95ee\u7ba1\u7406\u9762\u677f')),
                ('allow_edit_post', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u7f16\u8f91\u5e16\u5b50')),
                ('allow_stick_thread', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u7f6e\u9876\u4e3b\u9898')),
                ('allow_delete_post', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u5220\u9664\u5e16\u5b50')),
                ('allow_edit_user', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u7f16\u8f91\u7528\u6237')),
                ('allow_post_announce', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u53d1\u5e03\u7ad9\u70b9\u516c\u544a')),
                ('allow_view_log', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u67e5\u770b\u7ba1\u7406\u65e5\u5fd7')),
                ('allow_edit_forum', models.BooleanField(default=False, verbose_name='\u5141\u8bb8\u7f16\u8f91\u677f\u5757')),
                ('group', models.OneToOneField(verbose_name='\u6240\u5c5e\u7cfb\u7edf\u7528\u6237\u7ec4', to='users.Group')),
            ],
            options={
                'db_table': 'system_group_permissions',
                'verbose_name': '\u7cfb\u7edf\u7528\u6237\u7ec4\u6743\u9650',
                'verbose_name_plural': '\u7cfb\u7edf\u7528\u6237\u7ec4\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4', to='users.Group')),
                ('user', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_groups',
                'verbose_name': '\u7528\u6237\u4e0e\u7528\u6237\u7ec4\u8054\u63a5\u8868',
                'verbose_name_plural': '\u7528\u6237\u4e0e\u7528\u6237\u7ec4\u8054\u63a5\u8868',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
