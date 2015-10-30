# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0012_auto_20151030_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sigue',
            name='seguido',
        ),
        migrations.AddField(
            model_name='sigue',
            name='seguido',
            field=models.CharField(default='nadie', max_length=50),
            preserve_default=False,
        ),
    ]
