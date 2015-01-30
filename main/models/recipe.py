# -*- coding: utf-8 -*-
from django.db import models
from random import randrange

from meataggsmilk.settings import MEDIA_URL

class RecipeCategory(models.Model):
  name = models.CharField(u'название', max_length=100)
  image = models.ImageField(u'картинка')

  def get_image_display(self):
    return '<IMG src="%s%s" style="height:100px;width:100px;" />' % (MEDIA_URL, self.image)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'категория рецептов'
    verbose_name_plural = u'категории рецептов'

class RecipeManager(models.Manager):
  def getRandom(self):
    vol = self.count()
    return self.all()[randrange(vol)]

class Recipe(models.Model):
  name = models.CharField(u'название', max_length=100)
  smallImage = models.ImageField(u'маленькая картинка')
  bigImage = models.ImageField(u'большая картинка')
  coockingMethod = models.TextField(u'способ приготовления')
  category = models.ForeignKey(RecipeCategory, verbose_name=u'категория')

  objects = RecipeManager()

  def get_smallImage_display(self):
    return '<IMG src="%s%s" style="height:100px;width:100px;" />' % (MEDIA_URL, self.smallImage)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = u'рецепт'
    verbose_name_plural = u'рецепты'

class RecipeIngridient(models.Model):
  recipe = models.ForeignKey(Recipe, related_name='ingredients', verbose_name=u'рецепт')
  name = models.CharField(u'название', max_length=32)
  value = models.CharField(u'количество', max_length=16)

  def __unicode__(self):
    return '%s -- %s' % (self.name, self.value)

  class Meta:
    verbose_name = u'ингридеенты'
    verbose_name_plural = u'ингридеенты'
