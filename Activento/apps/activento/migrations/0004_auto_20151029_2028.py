# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0003_remove_usuario_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.ForeignKey(to='activento.Usuario'),
        ),
    ]
