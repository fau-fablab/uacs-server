# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20150924_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='fablabuser',
            name='name',
            field=models.CharField(default=b'fablabdau', max_length=200),
        ),
    ]
