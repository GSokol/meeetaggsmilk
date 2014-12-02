from django.template import RequestContext
from tools.decorators import render_to_response

from setts.models import TextModel, ImageModel
from main.models import RecipeCategory, Recipe, Good

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
  image = ImageModel.objexts.get(imgType=ImageModel.MAP).image
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
  goods = Good.objects.filter(in_resides__gt=0)
  return render_to_response("reside_list.html",
      {
        'goods': goods
      },
      RequestContext(request)
  )

def reside_good(request, id):
  good = None
  recipes = []
  descriptions = []
  value_choices = []

  try:
    good = Good.objects.get(pk=id)
    recipes = good.recipes.all()
    descriptions = good.description.split('\n')
    counter = 0;
    while counter <= good.in_resides:
      value_choices.append(counter)
      counter += good.step
  except Good.DoesNotExist:
    pass
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
  pass

def supply_good(request, id):
  pass

def supply_aditional_order(request):
  pass

# Orders
def supply_order(request):
  pass

def resides_order(request):
  pass

# Call order
def call_order(resquest):
  pass

# Search
def search(request):
  pass
