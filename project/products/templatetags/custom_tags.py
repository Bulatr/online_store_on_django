from django import template
from django.http import QueryDict

register = template.Library()

@register.simple_tag(takes_context=True)
def replace_query_param(context, param, value):
    request = context['request']
    query_params = request.GET.copy()
    query_params[param] = value
    return request.path + '?' + query_params.urlencode()