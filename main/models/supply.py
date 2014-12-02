# -*- coding: utf-8 -*-
from django.db import models

from datetime import date, datetime

from good import Good
from tools.fields import PriceField, ValueField, PhoneField

class SupplyManager(models.Manager):
  def getActual(self):
    supplies = self.filter(supplyDate__gt=date.today(), status=Supply.NEW)
    if len(supplies) == 0:
      return None
    return supplies[0]

class Supply(models.Model):
  NEW = 'new'
  ORDERED = 'ordered'
  WEIGHTED = 'weighted'
  RESIDED = 'resided'

  STATUSES = (
    (NEW, u'новая'),
    (ORDERED, u'заказаная'),
    (WEIGHTED, u'взвешенная'),
    (RESIDED, u'переведенная в остатки'),
  )
  supplyDate = models.DateField(u'дата поставки')
  status = models.CharField(u'статус', max_length=32, choices=STATUSES, default=NEW, editable=False)
  goods = models.ManyToManyField(Good, through='SupplyItem')
  
  objects = SupplyManager()

  def __unicode__(self):
    return '%s %s' % (self.supplyDate, self.get_status_display())

#  def save(self, *args, **kwargs):
    # Only one futre supply could exist and nobody should add past supplies
#    if ((kwargs.has_key('force_insert') and kwargs['force_insert']) or self.pk is None) \
#        and (self.supplyDate < date.today() or Supply.objects.filter(supplyDate__gt=date.today()).count() > 0):
#      return
#    super(Supply, self).save(*args, **kwargs)

  def delete(self, using=''):
    pass

  def turnToReside(self, deletePrevResides=False):
    for good in self.supplyitem_set.all():
      value = good.value
      for order in self.orders.all():
        if order.status != SupplyOrder.DELIVERED:
          return False
        for orderGood in order.supplyorderitem_set.all():
          if orderGood.good == good.good:
            value -= orderGood.value
      newGood = good.good.get()
      if deletePrevResides:
        newGood.in_resides = value
      else:
        newGood.in_resides += value
      newGood.save()
    return True

  class Meta:
    verbose_name=u'поставка'
    verbose_name_plural=u'поставки'

class SupplyItem(models.Model):
  supply = models.ForeignKey(Supply, verbose_name=u'поставка')
  good = models.ForeignKey(Good, verbose_name=u'товар')
  value = ValueField(u'количество')

  class Meta:
    verbose_name=u'пункт поставки'
    verbose_name_plural=u'пункты поставки'

class SupplyOrder(models.Model):
  NEW = 'new'
  PROCESSED = 'processed'
  WEIGHTED = 'weighted'
  DELIVERED = 'delivered'

  STATUSES = (
    (NEW, u'новый'),
    (PROCESSED, u'обработанный'),
    (WEIGHTED, u'взвешенный'),
    (DELIVERED, u'доставленный'),
  )

  timestamp = models.DateTimeField(u'дата/время', auto_now_add=True, editable=False)
  supply = models.ForeignKey(Supply, verbose_name=u'поставка', related_name='orders', editable=False, null=False, default=Supply.objects.getActual)
  phone = PhoneField(u'телефон')
  status = models.CharField(u'статус', max_length=16, default=NEW, choices=STATUSES)
  totalPrice = PriceField(u'итоговая стоимость', default=0, editable=False, max_digits=7)
  goods = models.ManyToManyField(Good, through='SupplyOrderItem')

  def save(self, *args, **kwargs):
    self.totalPrice = sum([x.value * x.good.price for x in self.supplyorderitem_set.all()])
    super(SupplyOrder, self).save(*args, **kwargs)

  def delete(self, using=''):
    pass

  def __unicode__(self):
    return u'%s %s %d руб. %s' % (self.phone, self.timestamp, self.totalPrice, self.get_status_display())

  class Meta:
    verbose_name = u'заказ на поставку'
    verbose_name_plural = u'заказы на поставку'

class SupplyOrderItem(models.Model):
  good = models.ForeignKey(Good, verbose_name=u'товар')
  order = models.ForeignKey(SupplyOrder, verbose_name=u'заказ')
  value = ValueField(u'количество')
  cut = models.BooleanField(u'разрезать', default=False)

  def save(self, *args, **kwargs):
    if not kwargs.pop('force', False):
      totalValue = 0
      actualSupply = Supply.objects.getActual()
      goodList = actualSupply.supplyitem_set.filter(good=self.good)
      if len(goodList) != 1:
        return
      totalValue += goodList[0].value
      for order in actualSupply.orders.exclude(pk=self.order.pk):
        for item in order.supplyorderitem_set.filter(good=self.good):
          totalValue -= item.value
          if totalValue < self.value:
            return False
      
    super(SupplyOrderItem, self).save(*args, **kwargs)
    self.order.save()

  class Meta:
    verbose_name = u'пункт заказа'
    verbose_name_plural = u'пункты заказа'
