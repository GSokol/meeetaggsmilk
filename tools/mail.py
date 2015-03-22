# -*- coding: utf-8 -*-

from os.path import join
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from meataggsmilk.settings import STATICFILES_DIRS, MEDIA_ROOT
from setts.models import ImageModel

def send(title, message, template, context, to):
  context['logo'] = ImageModel.objects.get(imgType = ImageModel.LOGO).image.filename
  if isinstance(to, basestring):
    message = EmailMultiAlternatives(title, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai', (to,))
    message.attach_alternative(render_to_string('mail/' + template, context))
    message.attach_file(join(STATICFILES_DIRS[0], 'img', 'background1.png'))
    message.attach_file(join(MEDIA_ROOT, context['logo']))
    message.send()
#    send_mail(title, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai',
#        (to,), html_message=render_to_string('mail/' + template, context))
  else:
    for addr in to:
      send(title, message, template, context, addr)
