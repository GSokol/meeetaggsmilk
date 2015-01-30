# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('admin/submit_line_custom.html', takes_context=True)
def submit_row(context):
  return {'actions': context['form_actions'] }
