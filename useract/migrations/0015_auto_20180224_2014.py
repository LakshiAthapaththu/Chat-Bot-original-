# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-24 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useract', '0014_auto_20180224_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserDetails',
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]