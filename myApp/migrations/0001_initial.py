# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fablabUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fauid', models.PositiveIntegerField(default=0)),
                ('Fraese', models.BooleanField()),
                ('Laser', models.BooleanField()),
            ],
        ),
    ]
