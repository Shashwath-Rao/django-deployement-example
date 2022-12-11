from django import template

register = template.Library()

@register.filter("cuts")
def cuts(value,args):
    return value.replace(args,"this")
