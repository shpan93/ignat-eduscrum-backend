# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ignat', '0002_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignat.Person'),
        ),
    ]