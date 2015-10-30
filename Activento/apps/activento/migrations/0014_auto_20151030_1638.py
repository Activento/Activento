# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0013_auto_20151030_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigue',
            name='seguido',
            field=models.ForeignKey(related_name='idolo', to='activento.Usuario'),
        ),
        migrations.RemoveField(
            model_name='sigue',
            name='seguir',
        ),
        migrations.AddField(
            model_name='sigue',
            name='seguir',
            field=models.ForeignKey(default='', to='activento.Usuario'),
            preserve_default=False,
        ),
    ]
