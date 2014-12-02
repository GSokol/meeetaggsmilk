from django.contrib import admin
from main.models import *

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'priceFut', 'in_resides', 'hidden', 'weekly',)
  list_filter = ('hidden',)

@admin.register(GoodCategory)
class GoodCategoryAdmin(admin.ModelAdmin):
  pass

@admin.register(ResidesOrder)
class ResidesOrderAdmin(admin.ModelAdmin):
  pass

@admin.register(ResidesOrderItem)
class ResidesOrderItemAdmin(admin.ModelAdmin):
  pass

@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
  readonly_fields = ('get_image_display',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  readonly_fields = ('get_smallImage_display',)

@admin.register(RecipeIngridient)
class RecipeIngridientAdmin(admin.ModelAdmin):
  pass

@admin.register(CallOrder)
class CallOrderAdmin(admin.ModelAdmin):
  pass

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
  pass

@admin.register(SupplyItem)
class SupplyItemAdmin(admin.ModelAdmin):
  pass

@admin.register(SupplyOrder)
class SupplyOrderAdmin(admin.ModelAdmin):
  pass

@admin.register(SupplyOrderItem)
class SupplyOrderItemAdmin(admin.ModelAdmin):
  pass
