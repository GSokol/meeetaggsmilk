# -*- coding: utf-8 -*-
from django.db import models

from datetime import date, datetime, timedelta

from good import Good
from order import Order
from tools.fields import PriceField, ValueField, PhoneField

class Partner(models.Model):
  MONDAY = 'mon'
  TUESDAY = 'tue'
  WENSDAY = 'wen'
  THURSDAY = 'thu'
  FRIDAY = 'fri'
  SATTURDAY = 'sat'
  SUNDEY = 'sun'
  ANY = 'any'

  DAYS = (
      (MONDAY, u'понедельник'),
      (TUESDAY, u'вторник'),
      (WENSDAY, u'среда'),
      (THURSDAY, u'четверг'),
      (FRIDAY, u'пятница'),
      (SATTURDAY, u'суббота'),
      (SUNDEY, u'воскресенье'),
      (ANY, u'любой день'),
  )

  WEEKDAYS = {
      MONDAY    : 0,
      TUESDAY   : 1,
      WENSDAY   : 2,
      THURSDAY  : 3,
      FRIDAY    : 4,
      SATTURDAY : 5,
      SUNDEY    : 6
  }

  name = models.CharField(u'имя', max_length=32)
  phone = PhoneField(u'телефон')
  deliveryDay = models.CharField(u'день доставки', max_length=32, choices=DAYS)
  invisiable = models.BooleanField(u'скрытый', default=False)

  def getFormActions(self):
    return [{
      'name'   : '_save',
      'value'  : u'Сохранить',
      'class'  : 'default'
    }, {
      'name'   : '__create_supply',
      'value'  : u'Создать новую поставку',
      'action' : 'createSupply'
    }, {
      'name'   : '_addanother',
      'value'  : u'Сохранить и добавить другой объект'
    }, {
      'name'   : '_continue',
      'value'  : u'Сохранить и продолжить редактирование'
    }]

  def __unicode__(self):
    return '%s: %s' % (self.name, self.phone)

  def toSupply(self, date_attr = None):
    if self.pk is None:
      return None
    if (self.deliveryDay is None or self.deliveryDay == self.ANY) and date_attr is None:
      return None
    if not date_attr is None:
      supply = Supply(partner=self,supplyDate=date_attr)
    else:
      futureSupplies = Supply.objects.filter(partner=self).filter(supplyDate__gt=date.today()).order_by('-supplyDate')
      if len(futureSupplies) == 0:
        lastDate = date.today()
      else:
        lastDate = futureSupplies[0].supplyDate
      deltaDays = (self.WEEKDAYS[self.deliveryDay] - lastDate.weekday() + 7) % 7
      if deltaDays <= 0:
        deltaDays += 7
      supplyDate = date.today() + timedelta(deltaDays)
      supply = Supply(partner=self, supplyDate=supplyDate)
      supply.save()
    for partnerGood in self.partnergood_set.all():
      if not partnerGood.defaultOrder is None:
        #TODO: Add check for unique
        SupplyItem(supply=supply, partnerGood=partnerGood, value=partnerGood.defaultOrder).save()
    return supply

  class Meta:
    verbose_name = u'партнер'
    verbose_name_plural = u'партнеры'

class PartnerGood(models.Model):
  partner = models.ForeignKey(Partner, verbose_name=u'партнер')
  name = models.CharField(u'название', max_length=32)
  price = PriceField(u'цена')
  minOrder = ValueField(u'минимальный заказ')
  step = ValueField(u'шаг', max_digits=3)
  maxOrder = ValueField(u'максимальный заказ', null=True, blank=True)
  defaultOrder = ValueField(u'стандартный заказ', null=True, blank=True)

  def minMargin(self):
    if self.pk is None:
      return 0
    margin = -1 * self.price
    margin += sum([x.good.price * x.value for x in self.partnergoodtogood_set.all()])
    return margin

  minMargin.short_description = u'минимальная маржа'

  def maxMargin(self):
    if self.pk is None:
      return 0;
    margin = -1 * self.price
    margin += sum([x.good.priceFut * x.value for x in self.partnergoodtogood_set.all()])
    return margin

  maxMargin.short_description = u'максимальная маржа'

  def __unicode__(self):
    return '%s: %s -- %d' % (self.partner.name, self.name, self.price)

  class Meta:
    verbose_name = u'товар поставщика'
    verbose_name_plural = u'товары поставщика'

class PartnerGoodToGood(models.Model):
  partnerGood = models.ForeignKey(PartnerGood, verbose_name=u'от поставщика')
  good = models.ForeignKey(Good, verbose_name=u'на прилавке')
  value = ValueField(u'количество')

  def __unicode__(self):
    return '%s = %s * %d' % (self.partnerGood.name, self.good.name, self.value)

  class Meta:
    verbose_name = u'поставщик/прилавок'
    verbose_name_plural = 'поставщики/прилавок'

class SupplyManager(models.Manager):
  def getActual(self):
    supplies = self.filter(supplyDate__gt=date.today(), status=Supply.NEW)
    if len(supplies) == 0:
      return None
    return supplies[0]

  def getByGoodPk(self, goodId):
    return self.raw('''SELECT s.* FROM main_partnergoodtogood pgg
      LEFT OUTER JOIN main_supplyitem si ON si.partnerGood_id = pgg.partnerGood_id
      LEFT OUTER JOIN main_supply s ON s.id = si.supply_id AND s.status<>"%s"
      WHERE pgg.good_id=%d''' % (Supply.WRITTEN_OFF, goodId))

class Supply(models.Model):
  NEW = 'new'
  ORDERED = 'ordered'
  WEIGHTED = 'weighted'
  WRITTEN_OFF = 'written-off'

  STATUSES = (
    (NEW, u'новая'),
    (ORDERED, u'заказаная'),
    (WEIGHTED, u'взвешенная'),
    (WRITTEN_OFF, u'списанная'),
  )

  partner = models.ForeignKey(Partner, verbose_name=u'партнер', editable=False)
  supplyDate = models.DateField(u'дата поставки')
  status = models.CharField(u'статус', max_length=32, choices=STATUSES, default=NEW, editable=False)
  partnerGoods = models.ManyToManyField(PartnerGood, through='SupplyItem')
  
  objects = SupplyManager()
  
  def listAvailableGoods(self, orderId=None):
    soldGoods = {}
    for supplyOrderItem in self.supplyorderitem_set.all():
      if (not orderId is None) and supplyOrderItem.pk == orderId:
        continue
      if soldGoods.has_key(supplyOrderItem.good.pk):
        soldGoods[supplyOrderItem.good.pk] += supplyOrderItem.value
      else:
        soldGoods[supplyOrderItem.good.pk] = supplyOrderItem.value
    allAvailableGoods = \
      [{ \
        'good': partnerGoodToGood.good, \
        'value': (supplyItem.partnerGood.maxOrder if supplyItem.isPartnerGood() and self.status == self.NEW \
          else (supplyItem.value * partnerGoodToGood.value)) - soldGoods.get(partnerGoodToGood.good.pk, 0), \
        'isPartnerGood' : supplyItem.isPartnerGood(),
        'supplyItem' : supplyItem,

      } for supplyItem in self.supplyitem_set.all() for partnerGoodToGood in supplyItem.partnerGood.partnergoodtogood_set.all()]
    return allAvailableGoods


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

  def getFormActions(self):
    if self.status == self.NEW:
      return [
          {
            'name': '__setorderd',
            'value': u'Заказать',
            'modelAction': 'order'
          }
      ]
    if self.status == self.ORDERED:
      return [
          {
            'name': '__setwheited',
            'value': u'Оприходовать',
            'modelAction': 'wheight'
          }
      ]
    if self.status == self.WEIGHTED \
        and (len(self.supplyorderitem_set.all()) == 0 or reduce(lambda a, b: a and b, map(lambda a: a.order.status == Order.WEIGHTED or a.order.status == Order.DELIVERED, self.supplyorderitem_set.all()))):
      return [
          {
            'name': '__setresided',
            'value': u'Списать остатки',
            'modelAction': 'wrightOff'
          }
      ]
    return []

  def order(self):
    if self.status == self.NEW:
      self.status = self.ORDERED

  def wheight(self):
    if self.status == self.ORDERED:
      self.status = self.WEIGHTED
      self.supplyorderitem_set.all().update(isWheightable=True)

  def wrightOff(self):
    if self.status == self.WEIGHTED \
        and reduce(lambda a, b: a and b, map(lambda a: a.status== SupplyOrder.WHEIGHTED or a.status == SupplyOrder.DELIVERED, self.orders.all())):
      self.status = self.WRITTEN_OFF

  class Meta:
    verbose_name=u'поставка'
    verbose_name_plural=u'поставки'

class SupplyItemManager(models.Manager):
  
  def getHotGoods(self):
    return self.__getGoods((Supply.ORDERED, Supply.WEIGHTED))

  def getActualGoods(self):
    return self.__getGoods((Supply.NEW, Supply.ORDERED, Supply.WEIGHTED))

  def __getGoods(self, statuses):
    supplyItems = self.filter(supply__status__in=statuses)\
        .order_by('supply__supplyDate')
    goods = []
    for supplyItem in supplyItems:
      for partnerGoodToGood in supplyItem.partnerGood.partnergoodtogood_set.all():
        orderedGoodSum = \
          sum([x.value for x in SupplyOrderItem.objects.filter(supply_id = supplyItem.supply.pk)\
              .filter(good_id=partnerGoodToGood.good.pk)])
        goods.append((partnerGoodToGood.good, partnerGoodToGood.value * supplyItem.value - orderedGoodSum, supplyItem.supply))
    return goods

class SupplyItem(models.Model):
  supply = models.ForeignKey(Supply, verbose_name=u'поставка')
  partnerGood = models.ForeignKey(PartnerGood, verbose_name=u'товар')
  value = ValueField(u'количество')

  objects = SupplyItemManager()

  def __unicode__(self):
    return '%s -- %d' % (self.partnerGood, self.value)

  def isPartnerGood(self):
    return (sum(map(lambda x: x.value + 1, self.partnerGood.partnergoodtogood_set.all())) == 2)

  def getOrders(self):
    if self.isPartnerGood():
      return sum(map(lambda x: x.value, self.supply.supplyorderitem_set.filter(good_id=self.partnerGood.partnergood_set.all()[0])))
    else:
      ret = ''
      for goodtogood in self.partnerGood.partnergoodtogood_set.all():
        ret += goodtogood.good.name + ': ' \
          + sum(map(lambda x: x.value, self.supply.supplyorderitem_set.filter(good_id=goodtogood.good.pk))) + '<BR />'
      return ret

  getOrders.short_description = u'заказано'

  def getResides(self, good=None):
    if good is None:
      return [{'good': partnerGoodToGood.good, 'value': self.value * partnerGoodToGood.value - sum([orderItem.value for orderItem in self.supply.supplyorderitem_set.filter(good=partnerGoodToGood.good)])} for partnerGoodToGood in self.partnerGood.partnergoodtogood_set.all()]
    else:
      return self.value * self.partnerGood.partnergoodtogood_set.filter(good=good)[0].value - sum([orderItem.value for orderItem in self.supply.supplyorderitem_set.filter(good_id=good.pk)])

  class Meta:
    verbose_name=u'пункт поставки'
    verbose_name_plural=u'пункты поставки'

class SupplyOrderItem(models.Model):
  good = models.ForeignKey(Good, verbose_name=u'товар')
  order = models.ForeignKey(Order, verbose_name=u'заказ')
  supply = models.ForeignKey(Supply, verbose_name=u'поставка')
  value = ValueField(u'количество')
  cut = models.BooleanField(u'разрезать', default=False)
  isWheightable = models.BooleanField(u'можно взвесить', default=False, editable=False)
  isFromResides = models.BooleanField(u'из остатков', editable=False)

  def save(self, *args, **kwargs):
    if self.isFromResides is None:
      self.isFromResides = self.supply.status == Supply.NEW
    if self.pk is None and not self.supply is None:
      self.isWheightable = (self.supply.status == Supply.WEIGHTED)
    if not kwargs.pop('force', False):
      shouldReturn = True
      goodList = self.supply.listAvailableGoods(self.pk)
      for goodEntity in goodList:
        if goodEntity['good'].pk == self.good.pk:
          if goodEntity['value'] >= self.value:
            shouldReturn = False
          break
      if shouldReturn:
        return
      
    super(SupplyOrderItem, self).save(*args, **kwargs)
    self.order.save()

  def price(self):
    if (self.good):
      return self.good.price if self.isFromResides else self.good.priceFut
    return ''

  def getPrice(self):
    return self.price() * self.value

  price.short_description = u'цена'

  class Meta:
    verbose_name = u'пункт заказа'
    verbose_name_plural = u'пункты заказа'

