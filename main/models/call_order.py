# -*- coding: utf-8 -*-
from django.db import models
from tools.fields import PhoneField

class CallOrder(models.Model):
  NEW = 'new'
  PROCESSED = 'processed'
  STATUSES = (
    (NEW, u'новая'),
    (PROCESSED, u'обработанная')
  )

  timestap = models.DateTimeField(u'дата\время создания', auto_now_add=True);
  phone = PhoneField(u'телефон')
  status = models.CharField(u'статус',max_length=16, choices=STATUSES, default=NEW)

  class Meta:
    verbose_name = u'заявка на звонок'
    verbose_name_plural = u'заявки на звонок'
