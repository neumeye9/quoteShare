# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_auto_20170628_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotesManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='quotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotecreator', to='belt_app.Users'),
        ),
    ]
