# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_pwd', models.TextField(max_length=160)),
                ('user_email', models.CharField(max_length=32, null=True)),
                ('login_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default='未分类', max_length=32),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='Content', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='Title', max_length=64),
        ),
    ]