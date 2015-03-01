# -*- coding: utf-8 -*-
from django.db import models
from validators import PhoneValidator

class PriceField(models.DecimalField):

  def __init__(self, verbose_name = None, name = None, max_digits=6, **kwargs):
    if not verbose_name is None:
      kwargs['verbose_name'] = verbose_name
    if not name is None:
      kwargs['name'] = name
    kwargs['max_digits'] = max_digits
    kwargs['decimal_places'] = 2
    super(PriceField, self).__init__(**kwargs)

class ValueField(models.DecimalField):

  def __init__(self, verbose_name = None, name = None, max_digits=6, **kwargs):
    if not verbose_name is None:
      kwargs['verbose_name'] = verbose_name
    if not name is None:
      kwargs['name'] = name
    kwargs['max_digits'] = max_digits
    kwargs['decimal_places'] = 3
    kwargs['default'] = 0
    super(ValueField, self).__init__(**kwargs)

class PhoneField(models.CharField):

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 17
    kwargs['validators'] = [PhoneValidator()]
    super(PhoneField, self).__init__(*args, **kwargs)
