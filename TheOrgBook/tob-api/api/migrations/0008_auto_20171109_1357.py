# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171109_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationorg',
            name='doingBusinessAsId',
        ),
        migrations.RemoveField(
            model_name='locationorg',
            name='locationId',
        ),
        migrations.RemoveField(
            model_name='locationorg',
            name='verifiableOrgId',
        ),
        migrations.AddField(
            model_name='location',
            name='doingBusinessAsId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='api.DoingBusinessAs'),
        ),
        migrations.AddField(
            model_name='location',
            name='verifiableOrgId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='api.VerifiableOrg'),
        ),
        migrations.DeleteModel(
            name='LocationOrg',
        ),
    ]
