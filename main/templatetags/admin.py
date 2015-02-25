# -*- coding: utf-8 -*-
from django import template
from django.contrib.admin.templatetags.admin_list \
        import result_headers, result_hidden_fields, results

register = template.Library()

@register.inclusion_tag('admin/submit_line_custom.html', takes_context=True)
def submit_row_custom(context):
  return {'actions': context['form_actions'] }

@register.inclusion_tag('admin/change_list_results.html')
def result_linked_list(cl):
  headers = list(result_headers(cl))
  num_sorted_fields = 0
  for h in headers:
    if h['sortable'] and h['sorted']:
      num_sorted_fields += 1
  return {'cl': cl,
    'result_hidden_fields': list(result_hidden_fields(cl)),
    'result_headers': headers,
    'num_sorted_fields': num_sorted_fields,
    'results': list(results(cl))}

