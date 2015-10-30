# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0009_auto_20151029_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pertenece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_cate', models.ManyToManyField(to='activento.Categoria')),
                ('nombre_usu', models.ManyToManyField(to='activento.Usuario')),
            ],
        ),
    ]
