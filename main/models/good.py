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

class GoodManager(models.Manager):
  def dropAllResides(self):
    from django.db import connection
    connection.cursor().execute('UPDATE main_good SET in_resides=0')

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
  inResides = ValueField(u'в остатках', name='in_resides')

  objects = GoodManager()

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

class ResidesOrder(models.Model):
  NEW = 'new'
  PROCESSED = 'processed'
  DELIVERED = 'delivered'

  STATUSES = (
    (NEW, u'новый'),
    (PROCESSED, u'обработанный'),
    (DELIVERED, u'доставленный'),
  )

  ts = models.DateTimeField(u'дата/время', auto_now_add = True, editable=False)
  phone = PhoneField(u'телефон')
  totalPrice = PriceField(u'итоговая стоимость', default=0, editable=False, max_digits=7)
  status = models.CharField(u'статус', choices=STATUSES, default=NEW, max_length=16)
  goods = models.ManyToManyField(Good, through='ResidesOrderItem')

  def save(self, *args, **kwargs):
  #Count total price
    self.totalPrice = sum([x.value * x.good.price for x in self.residesorderitem_set.all()])
    super(GoodOrder, self).save(*args, **kwargs)

  def delete(self, using=''):
    pass

  def __unicode__(self):
    return '%s %s %d %s' % (self.phone, self.ts, self.totalPrice, self.get_status_display())

  class Meta:
    verbose_name = u'заказ на остатки'
    verbose_name_plural = u'заказы на остатки'

class ResidesOrderItem(models.Model):
  order = models.ForeignKey(ResidesOrder, verbose_name=u'заказ')
  good = models.ForeignKey(Good, verbose_name=u'товар')
  value = ValueField(u'количество')
	
  def save(self, *args, **kwargs):
    totalValue = 0
    totalValue += self.good.in_resides
    for order in ResidesOrder.objects.exclude(pk=self.order.pk).exclude(status=ResidesOrder.DELIVERED).exclude(status=ResidesOrder.PROCESSED):
      for item in order.residesorderitem_set.filter(good__pk=self.good.pk):
        totalValue -= item.value
        if totalValue < self.value:
          return False

    super(ResidesOrderItem, self).save(*args, **kwargs)
    self.order.save()

  class Meta:
    verbose_name = u'пункт заказа на остатки'
    verbose_name_plural = u'пункты заказа на остатки'
