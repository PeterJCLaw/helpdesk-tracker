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

@register.filter
def static(file):
    '''
    Concatenate root of path to static files with the given file.
    This is BASE_URL + MEDIA_URL + file.
    '''

    return settings.BASE_URL + settings.MEDIA_URL + file

@register.tag
def static_url(parser, token):
    '''
    Return root of path to static files.
    This is BASE_URL + MEDIA_URL.
    '''

    return StaticUrl()

class StaticUrl(template.Node):
    def __init__(self):
        pass
    def render(self, c):
        return settings.BASE_URL + settings.MEDIA_URL

