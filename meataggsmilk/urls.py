from django.conf.urls import patterns, include, url
from django.contrib import admin

from main import views, views_admin
from meataggsmilk import settings

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'meataggsmilk.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^$', views.main, name='url_main'),
  url(r'^delivery/$', views.delivery, name="url_delivery"),
  url(r'^call_order/$', views.call_order, name='url_call_order'),

  # Recipes
  url(r'^recipes/$', views.recipes, name="url_recipe_categories"),
  url(r'^recipes/(?P<category_id>[0-9]+)/$', views.recipe_category, name='url_recipe_category'),
  url(r'^recipe/(?P<id>[0-9]+)/$', views.recipe, name="url_recipe"),

  # Recide goods
  url(r'^resides/$', views.resides, name='url_resides'),
  url(r'^resides/(?P<id>[0-9]+)/$', views.reside_good, name="url_reside_good"),

  # Supplies
  url(r'^supply/change_order/(?P<idToMove>[0-9]+)/(?P<idAfter>[0-9]*)/$', views_admin.move, name="url_move"),
  url(r'^supply/(?P<id>[0-9]+)/$', views.supply_good_category, name="url_supplies"),
  url(r'^supply/good/(?P<id>[0-9]+)/(?P<categoryId>[0-9]+)/$', views.supply_good, name="url_supply_good"),

  # Orders
  url(r'^order/create/$', views.supply_order, name='url_order'),
  url(r'^order/bill/(?P<id>[0-9]+)/$', views_admin.print_bill, name="url_print_bill"),

  # Admin
  url(r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
