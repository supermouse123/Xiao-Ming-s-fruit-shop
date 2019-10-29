from django import template
register = template.Library()


@register.simple_tag(name="func")
def func(dict1, dict2):
    dict2 = str(dict2)
    return dict1[dict2]["goods_number"]
