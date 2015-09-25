# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_fablabuser_kabelbinder'),
    ]

    operations = [
        migrations.AddField(
            model_name='fablabuser',
            name='Betreuer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
