# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_fablabuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fablabuser',
            name='Kabelbinder',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
