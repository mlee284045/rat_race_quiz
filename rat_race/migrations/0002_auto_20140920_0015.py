# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat_race', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='location_lat',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='runner',
            name='location_long',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
    ]
