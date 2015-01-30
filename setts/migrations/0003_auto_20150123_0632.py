# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setts', '0002_auto_20141123_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='imgType',
            field=models.CharField(max_length=32, verbose_name='\u0442\u0438\u043f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438', choices=[(b'promo_panner', '\u043a\u0430\u0434\u0440 \u043f\u0440\u043e\u043c\u043e \u0431\u0430\u043d\u043d\u0435\u0440\u0430'), (b'logo', '\u043b\u043e\u0433\u043e\u0442\u0438\u043f'), (b'logo_bw', '\u0447\u0435\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439 \u043b\u043e\u0433\u043e\u0442\u0438\u043f'), (b'map', '\u043a\u0430\u0440\u0442\u0430')]),
            preserve_default=True,
        ),
    ]
