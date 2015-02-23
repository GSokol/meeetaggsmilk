# -*- coding: utf-8 -*-
from django import template
from django.contrib.admin.templatetags.admin_list import result_list

register = template.Library()

@register.inclusion_tag('admin/submit_line_custom.html', takes_context=True)
def submit_row(context):
  return {'actions': context['form_actions'] }

@register.inclusion_tag('admin/change_list_results.html')
def result_linked_list(cl):
  _cl = []
  for item in cl:
    if item.after is None:
      _cl.append(item)
      break
  currentItem = _cl[0]
  while True:
    if currentItem.before is None:
      break
    currentItem = currentItem.before
    _cl.append(currentItem)
  return result_list(_cl)
