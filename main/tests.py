# -*- coding: utf-8 -*-
from django.test import TestCase
from models.good import *
from models.supply import *
from datetime import date, timedelta
# Create your tests here.

class GoodTestCase(TestCase):
  def setUp(self):
    goodCat = GoodCategory(name=u'тестовая категория')
    goodCat.save()

#    self.supply = Supply(supplyDate = date.today() + timedelta(days=1))
#    self.supply.save()

 #   self.supplyOrder = SupplyOrder(supply=self.supply, phone='+7(915)032-59-23')

    self.good = Good(name=u'тестовый товар', description=u'это тестовый товар', category=goodCat, priceFut=100, price=70, measureName='шт', step=1, maxRequest=10, in_resides=3)

  def test_dropAllResides(self):
    self.good.save()
    self.assertLess(0, Good.objects.get(pk=self.good.pk).in_resides)
    Good.objects.dropAllResides()
    self.assertEqual(0, Good.objects.get(pk=self.good.pk).in_resides)

class SupplyOrderTestCase(TestCase):
  def setUp(self):
    pass

  def test_totalPriceCount(self):
    pass

  def test_itemValueValidation(self):
    pass
