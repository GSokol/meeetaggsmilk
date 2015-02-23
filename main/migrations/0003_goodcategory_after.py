# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_goodcategory_after'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodcategory',
            name='after',
            field=models.OneToOneField(related_name='before', null=True, blank=True, to='main.GoodCategory', verbose_name='\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439'),
            preserve_default=True,
        ),
    ]
