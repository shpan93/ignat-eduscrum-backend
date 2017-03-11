# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ignat', '0003_auto_20170311_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignat.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ignat.Person')),
            ],
        ),
    ]