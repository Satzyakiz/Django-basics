from django import template

register = template.Library()

@register.filter(name='do')
def do1(value,arg):
    '''
    This cuts all values of arg from a string
    '''
    return value.replace(arg,'')

#register.filter('do',do1)
