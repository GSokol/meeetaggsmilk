# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin
from django.core.exceptions import ValidationError
from django.forms.formsets import all_valid
from django.http import HttpResponse

class CachedModelAdmin(ModelAdmin):
  __cache = {}
  
  def get_object(self, request, object_id):
    """
    Returns an 
    """
    queryset = self.get_queryset(request)
    model = queryset.model
    try:
      object_id = model._meta.pk.to_python(object_id)
      if self.__cache.has_key(model.__class__.__name__ + '__' + str(object_id)):
        return self.__cache[model.__class__.__name__ + '__' + str(object_id)]
      try:
        obj = queryset.get(pk=object_id)
        self.__cache[model.__class__.__name__ + '__' + str(object_id)] = obj
        return obj
      except model.DoesNotExist:
        return None
    except (ValidationError, ValueError):
      return None

class CustomChangeActionsModelAdmin(CachedModelAdmin):

  DELETE_FORM_ACTION = 'delete_form_action'
  form_change_actions = None

  def add_view(self, request, form_url='', extra_context=None):
    context = {}
    context.update(extra_context or {})
    context['form_actions'] = [{
        'name'  :'_save',
        'value' : u'Сохранить',
        'class' : 'default'
    }, {
        'name'  : '_addanother',
        'value' : u'Сохранить и добавить другой объект'
    }, {
        'name'  : '_continue',
        'value' : u'Сохранить и продолжить редактирование'
    }] 
    return super(CustomChangeActionsModelAdmin, self).add_view(request, form_url, context)

  def change_view(self, request, object_id, form_url='', extra_context=None):
    context = {}
    context.update(extra_context or {})
    if not self.form_change_actions is None:
      obj = self.get_object(request, object_id)
      if isinstance(self.form_change_actions, basestring) and self.form_change_actions in dir(obj):
        getFormActions = getattr(obj, self.form_change_actions)
        if callable(getFormActions):
          context['form_actions'] = getFormActions()
      else:
        context['form_actions'] = self.form_change_actions
      if self.DELETE_FORM_ACTION in context['form_actions']:
        context['form_actions'].remove(self.DELETE_FORM_ACTION)
        context['has_delete_permission'] = True
      else:
        context['has_delete_permission'] = False
      for actionConfig in context['form_actions']:
        if request.method == 'POST' and actionConfig.has_key('name') and actionConfig['name'] in request.POST \
            and (actionConfig.has_key('modelAction') or actionConfig.has_key('action')):
          ModelForm = self.get_form(request, obj)
          form = ModelForm(request.POST, request.FILES, instance=obj)
          if form.is_valid():
            form_validated = True
            new_object = self.save_form(request, form, change=True)
          else:
            form_validated = False
            new_object = form.instance
          formsets, inline_instances = self._create_formsets(request, new_object)
          if all_valid(formsets) and form_validated:
            if actionConfig.has_key('modelAction') and actionConfig['modelAction'] in dir(new_object):
              save_action = getattr(new_object, actionConfig['modelAction'])
              if callable(save_action):
                save_action()
            self.save_model(request, new_object, form, True)
            self.save_related(request, form, formsets, True)
            change_message = self.construct_change_message(request, form, formsets)
            self.log_change(request, new_object, change_message)
            if actionConfig.has_key('action') and actionConfig['action'] in dir(self):
              adminAction = getattr(self, actionConfig['action'])
              if callable(adminAction):
                ret = adminAction(request, [new_object])
                if isinstance(ret, HttpResponse):
									return ret
            return self.response_change(request, new_object)
    return super(CustomChangeActionsModelAdmin, self).change_view(request, object_id, form_url, context)

  change_form_template = "admin/change_form_template.html"
