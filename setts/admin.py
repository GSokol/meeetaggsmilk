from django.contrib import admin
from setts.models import *

@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
  pass

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
  readonly_fields = ('get_image_display',)

@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
  pass
