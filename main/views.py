# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response as django_render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from tools.decorators import render_to_response
from tools.mail import send
from meataggsmilk.settings import MEDIA_ROOT

from datetime import date, datetime, timedelta
import json, urllib2, os, base64

from setts.models import TextModel, ImageModel, IntModel
from main.models import RecipeCategory, Recipe, Good, GoodCategory, Order, SupplyItem, Supply, SupplyOrderItem, CallOrder

# Promo pages
def main(request):
  main_text = filter(lambda x: x != '', TextModel.objects.get(name=TextModel.MAIN_PAGE).text.split('\n'))
  images = map(lambda x: x.image, ImageModel.objects.filter(imgType=ImageModel.PROMO_BANNER))
  return render_to_response(
    "main.html",
    {'main_text': main_text, 'image_urls': images},
    RequestContext(request)
  )

def delivery(request):
  texts = filter(lambda x: x != '', TextModel.objects.get(name=TextModel.DELIVERY_PAGE).text.split('\n'))
  image = ImageModel.objects.get(imgType=ImageModel.MAP).image
  return render_to_response(
    "delivery.html",
    {'texts': texts, 'image': image},
    RequestContext(request)
  )

# Recipes
def recipes(request):
  recipes = RecipeCategory.objects.all()
  return render_to_response("recipe_category_list.html", {'recipes': recipes}, RequestContext(request))

def recipe_category(request, category_id):
  recipes = Recipe.objects.filter(category__pk=category_id)
  return render_to_response("recipe_category.html", {'recipes': recipes}, RequestContext(request))

def recipe(request, id):
  recipe = None
  paragraphs = []
  ingridients = []
  try:
    recipe = Recipe.objects.get(pk=id)
    paragraphs = filter(lambda x: x != '', recipe.coockingMethod.split('\n'))
    ingredients = recipe.ingredients.all()
  except Recipe.DoesNotExist:
    pass
  return render_to_response("recipe.html",
    {
      'recipe': recipe,
      'paragraphs': paragraphs,
      'ingredients': ingredients
    }, 
    RequestContext(request)
  )

# Resides
def resides(request):
  goods = map(lambda x: {'good': x[0], 'value':x[1]}, SupplyItem.objects.getHotGoods())
  return render_to_response("reside_list.html",
      {
        'goods': goods
      },
      RequestContext(request)
  )

def reside_good(request, id, from_supplies=False):
  id = int(id)
  good = filter(lambda x: x[0].pk == id, SupplyItem.objects.getHotGoods())[0]
  recipes = []
  descriptions = []
  value_choices = []

  recipes = good[0].recipes.all()
  descriptions = good[0].description.split('\n')
  counter = 0;
  while counter <= good[1]:
    value_choices.append(counter)
    counter += good[0].step
  return render_to_response("reside_good.html",
      {
        'good': good,
        'recipes': recipes,
        'descriptions': descriptions,
        'value_choices': value_choices
      },
      RequestContext(request)
  )

# Supplies
def supply_good_category(request, id):
  goods = []
  supplies = Supply.objects.exclude(status=Supply.WRITTEN_OFF).order_by('supplyDate')
  for supply in supplies:
    availableGoods = supply.listAvailableGoods()
    for availableGoodEntity in availableGoods:
      if availableGoodEntity['good'].category.pk != int(id):
        continue
      shouldAppend = True
      for good in goods:
        if good.pk == availableGoodEntity['good'].pk:
          shouldAppend = False
          break
      if shouldAppend:
        goods.append(availableGoodEntity['good'])
  return render_to_response("supply_list.html",
          { 'goods': goods, 'categoryId' : id},
          RequestContext(request)
  )

def supply_good(request, id, categoryId):
  try:
    good = Good.objects.get(pk=id)
    supplies = Supply.objects.getByGoodPk(int(id))
    descriptions = good.description.split('\n')
    available = 0
    availableResides = -1

    for supply in supplies:
      for goodEntity in supply.listAvailableGoods():
        if goodEntity['good'].pk == good.pk:
          if goodEntity['value'] > available:
            available = goodEntity['value']
            if supply.status != Supply.NEW:
              availableResides = available
    value_choices = []
    counter = 0
    while counter <= available:
      value_choices.append(counter)
      counter += good.step
    return render_to_response('supply_good.html', {
      'good'             : good,
      'descriptions'     : descriptions,
      'availableResides' : availableResides,
      'value_choices'    : value_choices
    }, RequestContext(request))
  except Good.DoesNotExist:
    raise Http404
  except Supply.DoesNotExist:
    raise Http404

def supply_aditional_order(request):
  pass

# Orders
@csrf_exempt
def supply_order(request):
  order = urllib2.unquote(request.POST.get('order', ''))
  phone = request.POST.get('phone', None)
  email = request.POST.get('email', None)
  name = request.POST.get('name', None)
  address = request.POST.get('address', None)
  deliveryCloseHour = IntModel.objects.filter(intType=IntModel.HOUR_DELIVERYCLOSE)[0].value
  freeDeliveryMinPrice = IntModel.objects.filter(intType=IntModel.FREE_DELIVERY_MIN_PRICE)[0].value
  deliveryPrice = IntModel.objects.filter(intType=IntModel.DELIVERY_PRICE)[0].value
  deliveryInterval = IntModel.objects.filter(intType=IntModel.MAX_DELIVERY_INTERVAL)[0].value

  if order == '':
    return HttpResponseRedirect(reverse('url_main'))
  order = json.loads(order)
  supplyGroups = []
  supplies = Supply.objects.all().order_by('supplyDate')
  for orderItem in order: 
    found = False
    for supply in supplies:
      supplyDate = supply.supplyDate
      if supplyDate < date.today():
        if datetime.now().hour<deliveryCloseHour:
          supplyDate = date.today()
        else:
          supplyDate = date.today() + timedelta(1)
      availableGoods = supply.listAvailableGoods()
      for availableGood in availableGoods:
        if availableGood['good'].pk == int(orderItem['id']) and float(availableGood['value']) >= float(orderItem['value']):
          found = True
          orderItem['name'] = availableGood['good'].name
          if availableGood['supplyItem'].supply.status != Supply.NEW:
            orderItem['price'] = availableGood['good'].price
          else:
            orderItem['price'] = availableGood['good'].priceFut
          orderItem['total'] = orderItem['value'] * orderItem['price']
          createNewGroup = True
          orderItem['supply'] = supply
          orderItem['modelGood'] = availableGood['good']
          orderItem['supplyItem'] = availableGood['supplyItem']
          orderItem['isPartnerGood'] = availableGood['isPartnerGood']
          for supplyGroup in supplyGroups:
            if (supplyDate - supplyGroup['minDate']).days < deliveryInterval \
                and (supplyGroup['maxDate'] - supplyDate).days < deliveryInterval:
              createNewGroup = False
              supplyGroup['goods'].append(orderItem)
              if supplyDate < supplyGroup['minDate']:
                supplyGroup['minDate'] = supplyDate
              elif supplyGroup['maxDate'] < supplyDate:
                supplyGroup['maxDate'] = supplyDate
              supplyGroup['totalPrice'] += orderItem['total']
              if orderItem['cut']:
                supplyGroup['totalPrice'] += 100;
              break
          if createNewGroup:
            supplyGroups.append({
              'goods': [orderItem],
              'minDate': supplyDate,
              'maxDate': supplyDate,
              'totalPrice': orderItem['total'] + 100 * orderItem['cut'],
              'delivery': False
            })
          break
      if found:
        break

  if phone is None or email is None:
    for supplyGroup in supplyGroups:
      if supplyGroup['totalPrice'] < freeDeliveryMinPrice:
        supplyGroup['totalPrice'] += deliveryPrice
        supplyGroup['delivery'] = True

    return render_to_response('card.html', { 'supplyGroups': supplyGroups, 'deliveryPrice': deliveryPrice }, RequestContext(request))
  else:
    for supplyGroup in supplyGroups:
      order = Order(phone=phone, email=email, name=name, address=address, deliveryDate=supplyGroup['maxDate'])
      order.save()

      for good in supplyGroup['goods']:
        if good['isPartnerGood']:
          resides = good['supplyItem'].getResides(good['modelGood'])
          if resides < good['value']:
            difference = good['value'] - resides
            good['supplyItem'].value += difference
            good['supplyItem'].save()
        SupplyOrderItem(
            good=good['modelGood'],
            order=order,
            supply=good['supply'],
            value=good['value'],
            cut=False
        ).save()
      logoName = ImageModel.objects.get(imgType=ImageModel.LOGO_BW)
      logo = ''
      with open(os.path.join(MEDIA_ROOT, logoName.image), 'rb') as image_file:
        logo = base64.b64encode(image_file.read())
      message = u'''Здравствуйте, %s!
      Ваш заказ №%d принят и ожидает обработки!
        
      Огромное спасибо!
      Искренне ваши, мясо-яйца-молоко!''' % (name, order.pk,)
      #send_mail(u'Заказ #%d' % order.pk, message, u'order@xn--80aredccldbby6d7fc.xn--p1ai', (order.email,))
      send(u'Заказ №%d' % order.pk, message, 'order.html', {
          'name' : name,
          'logo' : logo,
          'orderNumber' : order.pk,
          'sumPrice' : supplyGroup['totalPrice'],
          'items' : map(lambda x: { 'object': x[0], 'id': x[1]}, \
            [(supplyGroup['goods'][index], index + 1) for index in xrange(supplyGroup['goods'])]),
          'deliveryPrice' : deliveryPrice
      }, order.email)
    resp = HttpResponseRedirect(reverse("url_main"))
    resp.set_cookie('card', '', 3600)
    resp.set_cookie('lastCard', request.COOKIES['card'], 31536000)
    return resp
  

# Call order
def call_order(request):
  phone = request.POST['phone']
  CallOrder(phone=phone).save()
  return HttpResponse(json.dumps({'status': 'OK'}), content_type="application/json")

# Search
def search(request):
  pass
