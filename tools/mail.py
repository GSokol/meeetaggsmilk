# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send(title, message, template, context, to):
  if isinstance(to, basestring):
    send_mail(title, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai',
        (to,), html_message=render_to_string('mail/' + template, context))
  else:
    for addr in to:
      send(title, message, template, context, addr)
