# -*- coding: utf-8 -*-
from main.models.good import Good, GoodCategory
from main.models.recipe import Recipe
from setts.models import ImageModel, PhoneModel
from django import shortcuts

def render_to_response(template, var_dict, context):
  if not var_dict.has_key('weekly_product'):
    try:
      var_dict['weekly_product'] = Good.objects.filter(weekly=True)
      for good in var_dict['weekly_product']:
        if good.smallImage == '':
            good.smallImage = './default.png'
    except Good.DoesNotExist:
      pass
  if not var_dict.has_key('random_recipe'):
    var_dict['random_recipe'] = Recipe.objects.getRandom()
  if not var_dict.has_key('map'):
    var_dict['map'] = ImageModel.objects.filter(imgType=ImageModel.MAP)[0].image
  if not var_dict.has_key('good_categories'):
    var_dict['good_categories'] = [GoodCategory.objects.get(after_id__isnull=True)]
    while True:
      try:
        var_dict['good_categories'].append(var_dict['good_categories'][-1].before)
      except GoodCategory.DoesNotExist:
        break
  if not var_dict.has_key('logo_img'):
    var_dict['logo_img'] = ImageModel.objects.filter(imgType=ImageModel.LOGO)[0].image
  if not var_dict.has_key('phones'):
    var_dict['phones'] = map(lambda x: x.phone, PhoneModel.objects.all())
  return shortcuts.render_to_response(template, var_dict, context)
