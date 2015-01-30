# -*- coding: utf-8 -*-
from django.db import models
from recipe import Recipe

from tools.fields import ValueField, PriceField, PhoneField

class GoodCategory(models.Model):
  name = models.CharField(u'название', max_length=100)
  hidden = models.BooleanField(u'скрытый', default=False)

  def __unicode__(self):
    return self.name
  
  class Meta:
    verbose_name = u'категория товаров'
    verbose_name_plural = u'категории товаров'

class Good(models.Model):
  name = models.CharField(u'название', max_length=100)
  category = models.ForeignKey(GoodCategory, verbose_name=u'категория товара')
  description = models.TextField(u'описание')
  priceFut = PriceField(u'цена при заказе на поставку')
  price = PriceField(u'цена при заказе на остатки')
  measureName = models.CharField(u'единица измерения', max_length=16)
  step = ValueField(u'шаг', max_digits=3)
  maxRequest = ValueField(u'максимальный размер заявки')
  smallImage = models.ImageField(u'маленькая картинка')
  bigImage = models.ImageField(u'большая картинка')
  hidden = models.BooleanField(u'скрытый', default=False)
  weekly = models.BooleanField(u'продукт недели', default=False)
  recipes = models.ManyToManyField(Recipe, verbose_name=u'рецепты', blank=True)
#  inResides = ValueField(u'в остатках', name='in_resides')

  def delete(self, using=''):
    pass

  def save(self, *args, ** kwargs):
    if self.weekly:
      Good.objects.all().update(weekly=False)
    super(Good, self).save(*args, **kwargs)

  def __unicode__(self):
    return '%s -- %d (%d) %s' % (self.name, self.priceFut, self.price, self.measureName)

  class Meta:
    verbose_name = u'товар'
    verbose_name_plural = u'товары'
