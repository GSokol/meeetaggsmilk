# -*- coding: utf-8 -*-
from django.db import models

from tools.fields import PriceField, PhoneField
from tools.admin.options import CustomChangeActionsModelAdmin

from setts.models import IntModel

class Order(models.Model):
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
  phone = PhoneField(u'телефон')
  email = models.EmailField()
  name = models.CharField(u'Ф.И.О.', max_length=64, null=True)
  address = models.TextField(u'адрес')
  status = models.CharField(u'статус', max_length=16, default=NEW, choices=STATUSES, editable=False)
  totalPrice = PriceField(u'итоговая стоимость', default=0, editable=False, max_digits=7)
  deliveryDate = models.DateField(u'дата доставки', null=True, blank=True)
  freeDelivery = models.BooleanField(u'доставка бесплатно', editable=False)

  def save(self, *args, **kwargs):
    freeDeliveryMinPrice = IntModel.objects.filter(intType=IntModel.FREE_DELIVERY_MIN_PRICE)[0].value
    deliveryPrice = IntModel.objects.filter(intType=IntModel.DELIVERY_PRICE)[0].value
    self.totalPrice = sum([x.getPrice() for x in self.supplyorderitem_set.all()])
    if self.totalPrice < freeDeliveryMinPrice:
      self.freeDelivery = False
      self.totalPrice += deliveryPrice
    else:
      self.freeDelivery = True
    super(Order, self).save(*args, **kwargs)

  def delete(self, using=''):
    if self.status == self.NEW:
      super(Order, self).delete(using)

  def __unicode__(self):
    return u'%s %s %s %d руб. %s' % \
        (self.phone, self.email, self.timestamp, self.totalPrice, self.get_status_display())

  def getFormActions(self):
    if self.status == self.NEW:
      return [{
        'name'        : '__setprocessed',
        'value'       : u'уточнить',
        'modelAction' : 'processed'
      },
      CustomChangeActionsModelAdmin.DELETE_FORM_ACTION
      ]
    if self.status == self.PROCESSED:
      ret = [{
        'name'        : '_continue',
        'value'       : 'Сохранить и продолжить редактирование'
      }]
      if reduce(lambda a, b: a and b, [x.isWheightable for x in self.supplyorderitem_set.all()]):
        ret.insert(0, {
          'name'        : '__setweighted',
          'value'       : u'взвесить',
          'modelAction' : 'wheighted'
        })
      return ret
    if self.status == self.WEIGHTED:
      return [{
        'name'          : '__printbill',
        'value'         : u'распечатать счет-фактуру',
        'action'        : 'redirectToBillPage'
      }, {
        'name'          : '__setdelivered',
        'value'         : u'доставить',
        'modelAction'   : 'delivered'
      }]
    return []

  def processed(self):
    if self.status == self.NEW:
      self.status = self.PROCESSED

  def wheighted(self):
    if self.status == self.PROCESSED \
        and reduce(lambda a, b: a and b, [x.isWheightable for x in self.supplyorderitem_set.all()]):
      self.status = self.WEIGHTED

  def delivered(self):
    if self.status == self.WEIGHTED:
      self.status = self.DELIVERED

  class Meta:
    verbose_name = u'заказ'
    verbose_name_plural = u'заказы'
