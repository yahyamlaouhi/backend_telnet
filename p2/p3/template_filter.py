from django.template.defaulttags import register
from django.template.base import Library

# Custom template filter to get data from a dictionary using key in template

register = Library()
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)