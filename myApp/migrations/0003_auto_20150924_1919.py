# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_fablabuser_fernbedienung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fablabuser',
            name='Fernbedienung',
            field=models.PositiveIntegerField(default=42),
        ),
    ]
