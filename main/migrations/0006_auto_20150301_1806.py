# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tools.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_good_cuttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='maxRequest',
            field=tools.fields.ValueField(default=0, verbose_name='\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438', max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partnergood',
            name='defaultOrder',
            field=tools.fields.ValueField(decimal_places=3, default=0, max_digits=6, blank=True, null=True, verbose_name='\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partnergood',
            name='maxOrder',
            field=tools.fields.ValueField(decimal_places=3, default=0, max_digits=6, blank=True, null=True, verbose_name='\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partnergood',
            name='minOrder',
            field=tools.fields.ValueField(default=0, verbose_name='\u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437', max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partnergoodtogood',
            name='value',
            field=tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplyitem',
            name='value',
            field=tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplyorderitem',
            name='value',
            field=tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
    ]
