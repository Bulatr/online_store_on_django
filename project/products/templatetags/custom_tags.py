from django import template
from django.http import QueryDict
from urllib.parse import urlencode
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(takes_context=True)
def replace_query_param(context, param, value):
    request = context['request']
    query_params = request.GET.copy()
    query_params[param] = value
    return request.path + '?' + query_params.urlencode()

@register.filter
@stringfilter
def add_query_param(url, param_name, param_value):
    params = {param_name: param_value}
    query_string = urlencode(params)
    separator = '&' if '?' in url else '?'
    return f'{url}{separator}{query_string}'
