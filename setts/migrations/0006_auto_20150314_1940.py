# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setts', '0005_auto_20150221_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmodel',
            name='name',
            field=models.CharField(unique=True, max_length=32, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', choices=[(b'main_page', '\u0442\u0435\u043a\u0441\u0442 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'), (b'delivery_page', '\u0442\u0435\u043a\u0441\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'), (b'new_order_mail', '\u0442\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430')]),
            preserve_default=True,
        ),
    ]
