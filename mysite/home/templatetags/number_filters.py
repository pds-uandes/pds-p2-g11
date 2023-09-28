from django import template

register = template.Library()

@register.filter
def is_number(value):
    try:
        if value is None:
            return False
        float(value)
        return True
    except ValueError:
        return False
