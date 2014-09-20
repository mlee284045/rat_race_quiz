# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat_race', '0003_quiz_runners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='location_lat',
            field=models.DecimalField(default=36.1, null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='runner',
            name='location_long',
            field=models.DecimalField(default=-115.18, null=True, max_digits=6, decimal_places=2),
        ),
    ]
