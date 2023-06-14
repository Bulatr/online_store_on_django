from django import template
from django.http import QueryDict
from urllib.parse import urlencode
from django.template.defaultfilters import stringfilter

register = template.Library()

# Нормально работающий тег, который заменяет параметры url
@register.simple_tag(takes_context=True)
def replace_query_param(context, param, value):
    request = context['request']
    query_params = request.GET.copy()
    query_params.setlist(param, [value])
    return request.path + '?' + query_params.urlencode()

# на всякий случай оставил, некорректно работает
@register.simple_tag(takes_context=True)
def add_query_param_pagination(context, url):
    request = context['request']
    params = request.GET.copy()
    params.update(request.POST)  # Если используете и POST параметры
    # Исключаем параметр 'page' из словаря params
    # params.pop('page', None)
    query_string = urlencode(params)
    return f'{url}?{query_string}'

# не помню что это
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
