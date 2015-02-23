# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tools.validators
import tools.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestap', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430\\\u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('phone', tools.fields.PhoneField(max_length=17, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[tools.validators.PhoneValidator()])),
                ('status', models.CharField(default=b'new', max_length=16, verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', choices=[(b'new', '\u043d\u043e\u0432\u0430\u044f'), (b'processed', '\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u0430\u044f')])),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u0437\u0432\u043e\u043d\u043e\u043a',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0437\u0432\u043e\u043d\u043e\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('priceFut', tools.fields.PriceField(verbose_name='\u0446\u0435\u043d\u0430 \u043f\u0440\u0438 \u0437\u0430\u043a\u0430\u0437\u0435 \u043d\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0443', max_digits=6, decimal_places=2)),
                ('price', tools.fields.PriceField(verbose_name='\u0446\u0435\u043d\u0430 \u043f\u0440\u0438 \u0437\u0430\u043a\u0430\u0437\u0435 \u043d\u0430 \u043e\u0441\u0442\u0430\u0442\u043a\u0438', max_digits=6, decimal_places=2)),
                ('measureName', models.CharField(max_length=16, verbose_name='\u0435\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f')),
                ('step', tools.fields.ValueField(default=0, verbose_name='\u0448\u0430\u0433', max_digits=3, decimal_places=2)),
                ('maxRequest', tools.fields.ValueField(default=0, verbose_name='\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438', max_digits=5, decimal_places=2)),
                ('smallImage', models.ImageField(upload_to=b'', verbose_name='\u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True)),
                ('bigImage', models.ImageField(upload_to=b'', verbose_name='\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True)),
                ('hidden', models.BooleanField(default=False, verbose_name='\u0441\u043a\u0440\u044b\u0442\u044b\u0439')),
                ('weekly', models.BooleanField(default=False, verbose_name='\u043f\u0440\u043e\u0434\u0443\u043a\u0442 \u043d\u0435\u0434\u0435\u043b\u0438')),
                ('cuttable', models.BooleanField(default=True, verbose_name='\u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('hidden', models.BooleanField(default=False, verbose_name='\u0441\u043a\u0440\u044b\u0442\u044b\u0439')),
                ('after', models.OneToOneField(related_name='before', null=True, blank=True, to='main.GoodCategory', verbose_name='\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u043e\u0432',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430/\u0432\u0440\u0435\u043c\u044f')),
                ('phone', tools.fields.PhoneField(max_length=17, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[tools.validators.PhoneValidator()])),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(max_length=64, null=True, verbose_name='\u0424.\u0418.\u041e.')),
                ('address', models.TextField(verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('status', models.CharField(default=b'new', verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', max_length=16, editable=False, choices=[(b'new', '\u043d\u043e\u0432\u044b\u0439'), (b'processed', '\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u044b\u0439'), (b'weighted', '\u0432\u0437\u0432\u0435\u0448\u0435\u043d\u043d\u044b\u0439'), (b'delivered', '\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0439')])),
                ('totalPrice', tools.fields.PriceField(default=0, verbose_name='\u0438\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', editable=False, max_digits=7, decimal_places=2)),
                ('deliveryDate', models.DateField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438', blank=True)),
                ('freeDelivery', models.BooleanField(verbose_name='\u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0430 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e', editable=False)),
            ],
            options={
                'verbose_name': '\u0437\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0437\u0430\u043a\u0430\u0437\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u0438\u043c\u044f')),
                ('phone', tools.fields.PhoneField(max_length=17, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', validators=[tools.validators.PhoneValidator()])),
                ('deliveryDay', models.CharField(max_length=32, verbose_name='\u0434\u0435\u043d\u044c \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438', choices=[(b'mon', '\u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), (b'tue', '\u0432\u0442\u043e\u0440\u043d\u0438\u043a'), (b'wen', '\u0441\u0440\u0435\u0434\u0430'), (b'thu', '\u0447\u0435\u0442\u0432\u0435\u0440\u0433'), (b'fri', '\u043f\u044f\u0442\u043d\u0438\u0446\u0430'), (b'sat', '\u0441\u0443\u0431\u0431\u043e\u0442\u0430'), (b'sun', '\u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435'), (b'any', '\u043b\u044e\u0431\u043e\u0439 \u0434\u0435\u043d\u044c')])),
                ('invisiable', models.BooleanField(default=False, verbose_name='\u0441\u043a\u0440\u044b\u0442\u044b\u0439')),
            ],
            options={
                'verbose_name': '\u043f\u0430\u0440\u0442\u043d\u0435\u0440',
                'verbose_name_plural': '\u043f\u0430\u0440\u0442\u043d\u0435\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartnerGood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('price', tools.fields.PriceField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=6, decimal_places=2)),
                ('minOrder', tools.fields.ValueField(default=0, verbose_name='\u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437', max_digits=5, decimal_places=2)),
                ('step', tools.fields.ValueField(default=0, verbose_name='\u0448\u0430\u0433', max_digits=3, decimal_places=2)),
                ('maxOrder', tools.fields.ValueField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437')),
                ('defaultOrder', tools.fields.ValueField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437')),
                ('partner', models.ForeignKey(verbose_name='\u043f\u0430\u0440\u0442\u043d\u0435\u0440', to='main.Partner')),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartnerGoodToGood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=5, decimal_places=2)),
                ('good', models.ForeignKey(verbose_name='\u043d\u0430 \u043f\u0440\u0438\u043b\u0430\u0432\u043a\u0435', to='main.Good')),
                ('partnerGood', models.ForeignKey(verbose_name='\u043e\u0442 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430', to='main.PartnerGood')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a/\u043f\u0440\u0438\u043b\u0430\u0432\u043e\u043a',
                'verbose_name_plural': '\u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0438/\u043f\u0440\u0438\u043b\u0430\u0432\u043e\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('smallImage', models.ImageField(upload_to=b'', verbose_name='\u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('bigImage', models.ImageField(upload_to=b'', verbose_name='\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('coockingMethod', models.TextField(verbose_name='\u0441\u043f\u043e\u0441\u043e\u0431 \u043f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0440\u0435\u0446\u0435\u043f\u0442',
                'verbose_name_plural': '\u0440\u0435\u0446\u0435\u043f\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=b'', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0440\u0435\u0446\u0435\u043f\u0442\u043e\u0432',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0440\u0435\u0446\u0435\u043f\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngridient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('value', models.CharField(max_length=16, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('recipe', models.ForeignKey(related_name='ingredients', verbose_name='\u0440\u0435\u0446\u0435\u043f\u0442', to='main.Recipe')),
            ],
            options={
                'verbose_name': '\u0438\u043d\u0433\u0440\u0438\u0434\u0435\u0435\u043d\u0442\u044b',
                'verbose_name_plural': '\u0438\u043d\u0433\u0440\u0438\u0434\u0435\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplyDate', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('status', models.CharField(default=b'new', verbose_name='\u0441\u0442\u0430\u0442\u0443\u0441', max_length=32, editable=False, choices=[(b'new', '\u043d\u043e\u0432\u0430\u044f'), (b'ordered', '\u0437\u0430\u043a\u0430\u0437\u0430\u043d\u0430\u044f'), (b'weighted', '\u0432\u0437\u0432\u0435\u0448\u0435\u043d\u043d\u0430\u044f'), (b'written-off', '\u0441\u043f\u0438\u0441\u0430\u043d\u043d\u0430\u044f')])),
                ('partner', models.ForeignKey(editable=False, to='main.Partner', verbose_name='\u043f\u0430\u0440\u0442\u043d\u0435\u0440')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0430',
                'verbose_name_plural': '\u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=5, decimal_places=2)),
                ('partnerGood', models.ForeignKey(verbose_name='\u0442\u043e\u0432\u0430\u0440', to='main.PartnerGood')),
                ('supply', models.ForeignKey(verbose_name='\u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0430', to='main.Supply')),
            ],
            options={
                'verbose_name': '\u043f\u0443\u043d\u043a\u0442 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
                'verbose_name_plural': '\u043f\u0443\u043d\u043a\u0442\u044b \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplyOrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', tools.fields.ValueField(default=0, verbose_name='\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e', max_digits=5, decimal_places=2)),
                ('cut', models.BooleanField(default=False, verbose_name='\u0440\u0430\u0437\u0440\u0435\u0437\u0430\u0442\u044c')),
                ('isWheightable', models.BooleanField(default=False, verbose_name='\u043c\u043e\u0436\u043d\u043e \u0432\u0437\u0432\u0435\u0441\u0438\u0442\u044c', editable=False)),
                ('isFromResides', models.BooleanField(verbose_name='\u0438\u0437 \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432', editable=False)),
                ('good', models.ForeignKey(verbose_name='\u0442\u043e\u0432\u0430\u0440', to='main.Good')),
                ('order', models.ForeignKey(verbose_name='\u0437\u0430\u043a\u0430\u0437', to='main.Order')),
                ('supply', models.ForeignKey(verbose_name='\u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0430', to='main.Supply')),
            ],
            options={
                'verbose_name': '\u043f\u0443\u043d\u043a\u0442 \u0437\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u043f\u0443\u043d\u043a\u0442\u044b \u0437\u0430\u043a\u0430\u0437\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='supply',
            name='partnerGoods',
            field=models.ManyToManyField(to='main.PartnerGood', through='main.SupplyItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='main.RecipeCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ForeignKey(verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430', to='main.GoodCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='good',
            name='recipes',
            field=models.ManyToManyField(to='main.Recipe', verbose_name='\u0440\u0435\u0446\u0435\u043f\u0442\u044b', blank=True),
            preserve_default=True,
        ),
    ]
