# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib import admin
from django.template import RequestContext
from tools.admin import CustomChangeActionsModelAdmin
from main.models import *
from main.forms import SupplyForm

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'priceFut', 'hidden', 'weekly',)
  list_filter = ('hidden',)

@admin.register(GoodCategory)
class GoodCategoryAdmin(admin.ModelAdmin):
  change_list_template = "admin/custom_change_list.html"
  list_display = ('name', 'hidden', 'after',)

@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
  readonly_fields = ('get_image_display',)

class RecipeIngridientAdmin(admin.TabularInline):
  model = RecipeIngridient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  readonly_fields = ('get_smallImage_display',)
  inlines = [RecipeIngridientAdmin]

@admin.register(CallOrder)
class CallOrderAdmin(admin.ModelAdmin):
  pass

class PartnerGoodToGoodInline(admin.TabularInline):
  model = PartnerGoodToGood

@admin.register(PartnerGood)
class PartnerGoodAdmin(admin.ModelAdmin):
  readonly_fields = ('minMargin', 'maxMargin')
  inlines = [PartnerGoodToGoodInline,]


class PartnerGoodInline(admin.TabularInline):
  model = PartnerGood
  readonly_fields = ('minMargin', 'maxMargin')

@admin.register(Partner)
class PartnerAdmin(CustomChangeActionsModelAdmin):
  actions = ['createSupply']
  inlines = [PartnerGoodInline,]
  form_change_actions = 'getFormActions'

  def createSupply(self, request, queryset):
    for partner in queryset:
      partner.toSupply()
  
  createSupply.short_description = u'Создать новую поставку'

#@admin.register(SupplyItem)
class SupplyItemAdmin(admin.TabularInline):
  model = SupplyItem
  verbose_name = u'товар'
  verbose_name_plural = u'товары'
  readonly_fields = ('getOrders',)
  extra = 0

#@admin.register(SupplyOrderItem)
class SupplyOrderItemAdmin(admin.TabularInline):
  model = SupplyOrderItem
  readonly_fields = ('price',)

#class SupplyOrderInline(admin.TabularInline):
#  model = Order
#  readonly_fields = ('totalPrice', 'status', 'timestamp')
#  verbose_name = u'заказ'
#  verbose_name_plural = u'заказы'
#  extra = 0
#  can_delete = False

@admin.register(Supply)
class SupplyAdmin(CustomChangeActionsModelAdmin):
  form = SupplyForm
  readonly_fields = ('partner','status',)
  list_display = ('partner', 'supplyDate', 'status')
  form_change_actions = 'getFormActions'
  inlines = [SupplyItemAdmin,] #  SupplyOrderInline]

  def has_add_permission(self, request):
    return False

@admin.register(Order)
class OrderAdmin(CustomChangeActionsModelAdmin):
  readonly_fields = ('timestamp', 'totalPrice')
  list_display = ('name', 'phone', 'status', 'totalPrice')
  inlines = [SupplyOrderItemAdmin]
  form_change_actions = 'getFormActions'

  def redirectToBillPage(self, request, queryset):
    return render_to_response(
        'admin/open_bill_windows.html',
        {'orders': [q.pk for q in queryset], 'referer': request.META['HTTP_REFERER']},
        RequestContext(request)
    )

  def processed(self, request, queryset):
    for order in queryset:
      order.processed()
      order.save()
      message = u'''Здравствуйте, %s!
      Ваш заказ №%d на сумму %.2f обработан!

      Огромное спасибо!
      Искренне ваши, мясо-яйца-молоко!''' % (order.name, order.pk, order.totalPrice)
#      send(u'Заказ №%d' % order.pk(), message, 
    return ''
