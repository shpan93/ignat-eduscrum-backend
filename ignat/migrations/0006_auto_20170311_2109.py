# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ignat', '0005_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ignat.Person'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estimate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(null=True),
        ),
    ]
