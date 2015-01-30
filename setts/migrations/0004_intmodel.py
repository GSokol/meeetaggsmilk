# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setts', '0003_auto_20150123_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intType', models.CharField(max_length=32, verbose_name='\u0442\u0438\u043f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439')),
                ('value', models.IntegerField(verbose_name='\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f',
                'verbose_name_plural': '\u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435',
            },
            bases=(models.Model,),
        ),
    ]
