# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_fablabuser_betreuer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fablabuser',
            old_name='name',
            new_name='Name',
        ),
    ]
