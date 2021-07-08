from django import template

register = template.Library()


@register.filter(name='loppcount')
def loppcount(number):
    try:
        for i in range(0, 100):
            return number[i]
    except:
        return False
