from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def colorize(val):
    sign = str(val)[:1]
    if sign == "-":
        html_string = f"<span style='color:green'>{val}</span>"
    elif sign == "0":
        html_string = f"<span style='color:blue'>{val}</span>"
    else:
        html_string = f"<span style='color:red'>{val}</span>"
    
    return mark_safe(html_string)