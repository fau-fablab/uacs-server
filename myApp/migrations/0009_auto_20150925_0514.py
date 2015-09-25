# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20150925_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fablabuser',
            name='fauid',
            field=models.CharField(default=b'faudauid', max_length=10),
        ),
    ]
