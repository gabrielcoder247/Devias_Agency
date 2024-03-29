# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-22 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='profile/')),
                ('email', models.TextField(blank=True, max_length=200, null=True)),
                ('blog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dev_apps.Blog')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
