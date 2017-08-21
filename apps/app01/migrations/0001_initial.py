# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('java', models.FloatField(max_length=50)),
                ('python', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='score_info',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.app01.User_Info'),
        ),
    ]
