# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0011_auto_20151030_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
