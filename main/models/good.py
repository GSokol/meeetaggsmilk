# -*- coding: utf-8 -*-
from django.db import models, transaction
from recipe import Recipe

from tools.fields import ValueField, PriceField, PhoneField

class GoodCategoryManager(models.Manager):

  @transaction.atomic
  def changeOrder(self, goodCategory1, goodCategory2):
    beforeFirst = goodCategory1.after
    afterFirst = self.get(after_id=goodCategory1.pk)
    afterSecond = self.get(after_id=goodCategory2.pk)
    
    goodCategory1.after = goodCategory2.after
    goodCategory2.after = beforeFirst
    
    afterFirst.after=goodCategory2
    afterFirst.save()
    
    afterSecond.after=goodCategory1
    afterSecond.save()
    
    goodCategory1.save()
    goodCategory2.save()
    
    return

class GoodCategory(models.Model):
  name = models.CharField(u'название', max_length=100)
  after = models.OneToOneField('self', related_name='before', verbose_name=u'предыдущий', null=True, blank=True)
  hidden = models.BooleanField(u'скрытый', default=False)

  objects = GoodCategoryManager()
  def __unicode__(self):
    return self.name

  def save(self, *args, **kwargs):
    if kwargs.get('skip_reordering', False):
      kwargs.pop('skip_reordering')
      return super(GoodCategory, self).save(*args, **kwargs)
    if self.pk is None:
      currentGoodCategory = super(GoodCategory, self).save(*args,**kwargs)
      GoodCategory.objects.filter(after_id = currentGoodCategory.after.pk) \
        .exclude(pk=currentGoodCategory.pk).update(after_id= currentGoodCategory.pk)
    else:
      oldGoodCategory = GoodCategory.objects.get(pk=self.pk)
      if oldGoodCategory.after == self.after or (oldGoodCategory.after is None and self.after is None):
        super(GoodCategory, self).save(*args, **kwargs)
      elif oldGoodCategory.after is None:
        before = oldGoodCategory.before
        before.after = None
        before.save(skip_reordering=True)

        before = GoodCategory.objects.get(after_id=self.after.pk)
        before.after = self
        before.save(skip_reordering=True)

        super(GoodCategory, self).save(*args, **kwargs)
      elif self.after is None:
        after = GoodCategory.objects.get(after_id__isnull=True)
        super(GoodCategory, self).save(*args, **kwargs)

        before = oldGoodCategory.before
        before.after = oldGoodCategory.after
        before.save(skip_reordering=True)

        after.after = self.pk
        after.save(skip_reordering=True)

      else:
        afterOld = oldGoodCategory.after
        beforeOld = oldGoodCategory.before
        beforeOld.after = None
        beforeOld.save(skip_reordering=True)

        beforeNew = GoodCategory.objects.get(after_id=self.after.pk)
        beforeNew.after = self
        beforeNew.save(skip_reordering=True)

        super(GoodCategory, self).save(*args, **kwargs)

        beforeOld.after = afterOld
        beforeOld.save(skip_reordering=True)

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
  smallImage = models.ImageField(u'маленькая картинка', blank=True)
  bigImage = models.ImageField(u'большая картинка', blank=True)
  hidden = models.BooleanField(u'скрытый', default=False)
  weekly = models.BooleanField(u'продукт недели', default=False)
  recipes = models.ManyToManyField(Recipe, verbose_name=u'рецепты', blank=True)
  cuttable = models.BooleanField(u'можно разделать', default=True)
#  inResides = ValueField(u'в остатках', name='in_resides')

  def delete(self, using=''):
    pass

  def save(self, *args, **kwargs):
    if self.weekly:
      Good.objects.all().update(weekly=False)
    super(Good, self).save(*args, **kwargs)

  def __unicode__(self):
    return '%s -- %d (%d) %s' % (self.name, self.priceFut, self.price, self.measureName)

  class Meta:
    verbose_name = u'товар'
    verbose_name_plural = u'товары'
