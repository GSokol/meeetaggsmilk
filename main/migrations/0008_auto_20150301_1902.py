# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150301_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['name'], 'verbose_name': '\u0442\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b'},
        ),
    ]
