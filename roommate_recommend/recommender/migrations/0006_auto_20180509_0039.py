# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 00:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0005_auto_20180509_0034'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dislikehousing',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='dislikehousing',
            name='house',
        ),
        migrations.RemoveField(
            model_name='dislikehousing',
            name='user',
        ),
        migrations.DeleteModel(
            name='DisLikeHousing',
        ),
    ]
