# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fablabuser',
            name='Fernbedienung',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
