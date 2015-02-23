# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_good_cuttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='cuttable',
            field=models.BooleanField(default=True, verbose_name='\u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0430\u0442\u044c'),
            preserve_default=True,
        ),
    ]
