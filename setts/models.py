# -*- coding: utf-8 -*-
from django.db import models
from tools.fields import PhoneField
from meataggsmilk.settings import MEDIA_URL

class TextModel(models.Model):
  MAIN_PAGE = 'main_page'
  DELIVERY_PAGE = 'delivery_page'
  BILL_TEXT = 'bill_text'
  NEW_ORDER_MAIL = 'new_order_mail'
  CHOICES = (
    (MAIN_PAGE, u'текст главной страницы'),
    (BILL_TEXT, u'текст на счете'),
    (DELIVERY_PAGE, u'текст страницы доставки'),
    (NEW_ORDER_MAIL, u'текст письма нового заказа'),
  )
  name = models.CharField(u'название', max_length=32, choices=CHOICES, unique=True)
  text = models.TextField(u'текст')

  def __unicode__(self):
    return '%s' % self.get_name_display()

  class Meta:
    verbose_name = u'текст'
    verbose_name_plural = u'тексты'

class ImageModel(models.Model):
  PROMO_BANNER = 'promo_panner'
  LOGO = 'logo'
  LOGO_BW = 'logo_bw'
  MAP = 'map'

  CHOICES = (
    (PROMO_BANNER, u'кадр промо баннера'),
    (LOGO, u'логотип'),
    (LOGO_BW, u'черно-белый логотип'),
    (MAP, u'карта'),
  )

  imgType = models.CharField(u'тип картинки', max_length=32, choices=CHOICES)
  image = models.ImageField(u'картинка')

  def __unicode__(self):
    return self.get_imgType_display()

  def get_image_display(self):
    if self.imgType == self.LOGO:
        return '<IMG src="%s%s" style="height:268px;width:400px;" />' % (MEDIA_URL, self.image)
    return '<IMG src="%s%s" />' % (MEDIA_URL, self.image)
  
  get_image_display.shoort_description = u'картинка'
  get_image_display.allow_tags = True

  class Meta:
    verbose_name = u'картинка'
    verbose_name_plural = u'картинки'

class PhoneModel(models.Model):
  phone = PhoneField(u'телефон')

  def __unicode__(self):
    return self.phone

  class Meta:
    verbose_name = u'телефон'
    verbose_name_plural = u'телефоны'

class IntModel(models.Model):
  MAX_DELIVERY_INTERVAL = 'max_delivery_interval'
  DELIVERY_PRICE = 'delivery_price'
  FREE_DELIVERY_MIN_PRICE = 'free_delivery_min_price'
  HOUR_DELIVERYCLOSE ='hour_delivery_close'

  TYPES = (
      (MAX_DELIVERY_INTERVAL, u'максимальный интервал между поставками'),
      (DELIVERY_PRICE, u'Цена платной доставки'),
      (FREE_DELIVERY_MIN_PRICE, u'Минимальная цена бесплатной доставки'),
      (HOUR_DELIVERYCLOSE, u'Час закрытия доставки в тот же день'),
  )

  intType = models.CharField(u'тип переменной', max_length=32, choices=TYPES)
  value = models.IntegerField(u'значение')

  def __unicode__(self):
    return '%s: %d' % (self.get_intType_display(), self.value)

  class Meta:
    verbose_name = u'переменная'
    verbose_name_plural = u'переменные'
