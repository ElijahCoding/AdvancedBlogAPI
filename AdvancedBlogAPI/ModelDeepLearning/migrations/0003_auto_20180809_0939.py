# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-09 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelDeepLearning', '0002_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='languages',
            field=models.ManyToManyField(to='ModelDeepLearning.Language'),
        ),
    ]
