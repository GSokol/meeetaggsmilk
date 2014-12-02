# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tools.fields
import tools.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imgType', models.CharField(max_length=32, verbose_name='\u0442\u0438\u043f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438')),
                ('image', models.ImageField(upload_to=b'', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430',
                'verbose_name_plural': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', tools.fields.PhoneField(max_length=16, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[tools.validators.PhoneValidator()])),
            ],
            options={
                'verbose_name': '\u0442\u0435\u043b\u0435\u0444\u043e\u043d',
                'verbose_name_plural': '\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', choices=[(b'main_page', '\u0442\u0435\u043a\u0441\u0442 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'), (b'delivery_page', '\u0442\u0435\u043a\u0441\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')])),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442')),
            ],
            options={
                'verbose_name': '\u0442\u0435\u043a\u0441\u0442',
                'verbose_name_plural': '\u0442\u0435\u043a\u0441\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
