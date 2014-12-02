from django.conf.urls import patterns, include, url
from django.contrib import admin

from main import views
from meataggsmilk import settings

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'meataggsmilk.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^$', views.main, name='url_main'),

  # Recipes
  url(r'^recipes/$', views.recipes, name="url_recipe_categories"),
  url(r'^recipes/(?P<category_id>[0-9]+)/$', views.recipe_category, name='url_recipe_category'),
  url(r'^recipe/(?P<id>[0-9]+)/$', views.recipe, name="url_recipe"),

  # Recide goods
  url(r'^recides/$', views.resides, name='url_resides'),
  url(r'resides/(?P<id>[0-9]+)/$', views.reside_good, name="url_reside_good"),

  # Admin
  url(r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
