# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activento', '0006_auto_20151029_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sigue',
            old_name='nombre1s',
            new_name='seguir',
        ),
        migrations.AddField(
            model_name='sigue',
            name='seguido',
            field=models.ManyToManyField(related_name='topic_content_type', to='activento.Usuario'),
        ),
    ]
