# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tools.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150301_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='step',
            field=tools.fields.ValueField(default=0, verbose_name='\u0448\u0430\u0433', max_digits=4, decimal_places=3),
            preserve_default=True,
        ),
    ]
