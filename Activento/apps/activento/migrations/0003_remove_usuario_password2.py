# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0002_auto_20151029_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password2',
        ),
    ]
