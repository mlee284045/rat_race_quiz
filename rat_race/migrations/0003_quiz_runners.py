# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rat_race', '0002_auto_20140920_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='runners',
            field=models.ForeignKey(related_name=b'quiz', default=1, to='rat_race.Runner'),
            preserve_default=False,
        ),
    ]
