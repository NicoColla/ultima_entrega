from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter
def custom_format(value):
    if value is None:
        return ""
    try:
        value = float(value)
    except ValueError:
        return value

    return "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")