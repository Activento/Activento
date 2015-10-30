# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0007_auto_20151029_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigue',
            name='seguido',
            field=models.ManyToManyField(related_name='topic_content_type2', to='activento.Usuario'),
        ),
    ]
