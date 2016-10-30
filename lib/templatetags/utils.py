from django import template

register = template.Library()


@register.simple_tag(name='mul')
def mul(val, arg):
    return val * arg
