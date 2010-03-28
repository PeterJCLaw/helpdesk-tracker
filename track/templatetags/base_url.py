from django.conf import settings
from django import template

register = template.Library()

@register.filter
def base(file):
    '''
    Concatenate BASE_URL and file.
    '''

    return settings.BASE_URL + file

@register.tag
def base_url(parser, token):
    '''
    Concatenate BASE_URL and file.
    '''

    return BaseUrl()

class BaseUrl(template.Node):
    def __init__(self):
        pass
    def render(self, c):
        return settings.BASE_URL

