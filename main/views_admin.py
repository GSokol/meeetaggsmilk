# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import Http404, response
from django.shortcuts import render_to_response
from django.contrib.auth import get_permission_codename
from django.db import transaction

from setts.models import IntModel, ImageModel
from main.models import Order, GoodCategory

from datetime import date

def print_bill(request, id):
  try:
    deliveryPrice = IntModel.objects.filter(intType=IntModel.DELIVERY_PRICE)[0].value

    order = Order.objects.get(pk=id)
    logo = ImageModel.objects.get(imgType=ImageModel.LOGO_BW)
    num = 1
    items = []
    deliveryDate = None
    for item in order.supplyorderitem_set.all():
      if item.isFromResides:
        items.append((num, item.good.name, item.good.price, item.value, round(item.value * item.good.price, 2)))
      else:
        items.append((num, item.good.name, item.good.priceFut, item.value, '{:.2f}'.format(item.value * item.good.priceFut, True)))
      num += 1
      if item.cut:
        items.append((num, u'порезать', '300.00', 1, '300.00'))
        num += 1
    if deliveryDate is None or deliveryDate < item.supply.supplyDate:
      deliveryDate = item.supply.supplyDate

    return render_to_response('admin/bill.html', {
        'logo'          : logo.image,
        'items'         : items,
        'sumPrice'      : order.totalPrice,
        'date'          : date.today().strftime('%d/%m/%Y'),
        'orderDate'     : order.timestamp.strftime('%d/%m/%Y'),
        'deliveryDate'  : deliveryDate.strftime('%d/%m/%Y') if deliveryDate > date.today() else date.today().strftime('%d/%m/%Y'),
        'deliveryPrice' : deliveryPrice if not order.freeDelivery else False
      }, RequestContext(request))
  except Order.DoesNotExist:
    raise Http404

@transaction.atomic
def move(request, idToMove, idAfter):
  if request.user.has_perm('%s.%s' \
          % (GoodCategory._meta.app_label, get_permission_codename('change', GoodCategory._meta))):
    obj = GoodCategory.objects.get(pk=idToMove)
    obj.after = GoodCategory.objects.get(pk=idAfter)
    obj.save()
    return response.HttpResponse()
  return response.HttpResponseForbidden()
