# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator

class PhoneValidator(RegexValidator):
  def __init__(self):
    super(PhoneValidator, self)\
      .__init__(r'^\+7\([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}$', u'Неправильный номер телефона')
