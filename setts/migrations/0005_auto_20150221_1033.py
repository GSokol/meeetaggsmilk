# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setts', '0004_intmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intmodel',
            name='intType',
            field=models.CharField(max_length=32, verbose_name='\u0442\u0438\u043f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439', choices=[(b'max_delivery_interval', '\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0430\u043c\u0438'), (b'delivery_price', '\u0426\u0435\u043d\u0430 \u043f\u043b\u0430\u0442\u043d\u043e\u0439 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'), (b'free_delivery_min_price', '\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\u0439 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'), (b'hour_delivery_close', '\u0427\u0430\u0441 \u0437\u0430\u043a\u0440\u044b\u0442\u0438\u044f \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u0432 \u0442\u043e\u0442 \u0436\u0435 \u0434\u0435\u043d\u044c')]),
            preserve_default=True,
        ),
    ]
