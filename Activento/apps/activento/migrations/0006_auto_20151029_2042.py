# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0005_auto_20151029_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='sigue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre1s', models.ManyToManyField(to='activento.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
