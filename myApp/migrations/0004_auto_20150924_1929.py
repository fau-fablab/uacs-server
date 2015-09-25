# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20150924_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fablabuser',
            name='Fernbedienung',
            field=models.BooleanField(),
        ),
    ]
