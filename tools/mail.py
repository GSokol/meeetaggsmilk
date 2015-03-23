# -*- coding: utf-8 -*-

from os.path import join, basename

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from smtplib import SMTP
import email.Charset

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from meataggsmilk.settings import STATICFILES_DIRS, MEDIA_ROOT, EMAIL_HOST, EMAIL_HOST_USER, \
    EMAIL_HOST_PASSWORD, EMAIL_PORT
from setts.models import ImageModel

def send(title, message, template, context, to):
  email.Charset.add_charset('utf-8', email.Charset.SHORTEST, None, None)

  if isinstance(to, basestring):
    context['logo'] = basename(ImageModel.objects.get(imgType = ImageModel.LOGO).image.name)
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = title
    msgRoot['From'] = u'Магазин фермерских продуктов <order@мясояйцамооко.рф>'
    msgRoot['To'] = to

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgAlternative.attach(MIMEText(message, _charset='utf-8'))
    msgAlternative.attach(MIMEText(render_to_string('mail/' + template, context), 'html', _charset='utf-8'))

    fp = open(join(STATICFILES_DIRS[0], 'img', 'background1.jpg'), 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<background1.jpg>')
    msgRoot.attach(msgImage)

    fp = open(join(MEDIA_ROOT, context['logo']), 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<' + context['logo'] + '>')
    msgRoot.attach(msgImage)

    smtp = SMTP()
    smtp.connect(EMAIL_HOST + ':' + EMAIL_PORT)
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.sendmail(EMAIL_HOST_USER, to, msgRoot.as_string())
    smtp.quit()

#    message = EmailMultiAlternatives(title, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai', (to,))
#    message.attach_alternative(, 'text/html')
#    message.attach_file(join(STATICFILES_DIRS[0], 'img', 'background1.jpg'), 'image/jpeg')
#    message.attach_file(join(MEDIA_ROOT, context['logo']), 'image/png')
#    message.send()
#    send_mail(title, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai',
#        (to,), html_message=render_to_string('mail/' + template, context))
  else:
    for addr in to:
      send(title, message, template, context, addr)
