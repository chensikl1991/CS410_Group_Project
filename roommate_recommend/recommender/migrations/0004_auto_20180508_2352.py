# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 23:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0003_roommatepreference_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeHousing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='housing',
            name='user',
        ),
        migrations.AlterField(
            model_name='roommatepreference',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likehousing',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommender.Housing', verbose_name='housing_like'),
        ),
        migrations.AddField(
            model_name='likehousing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommender.UserProfile', verbose_name='user_like'),
        ),
        migrations.AlterUniqueTogether(
            name='likehousing',
            unique_together=set([('user', 'house')]),
        ),
    ]
