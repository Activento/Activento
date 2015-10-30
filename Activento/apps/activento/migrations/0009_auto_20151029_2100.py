# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0008_auto_20151029_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='sigue',
            name='seguido',
            field=models.ManyToManyField(related_name='seguido', to='activento.Usuario'),
        ),
    ]
