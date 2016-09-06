# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_id', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('C', 'Contract'), ('G', 'Grant'), ('DP', 'Direct Payment'), ('L', 'Loan')], max_length=5)),
            ],
            options={
                'db_table': 'awards',
            },
        ),
    ]
