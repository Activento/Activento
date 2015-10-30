# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0010_pertenece'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
