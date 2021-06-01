from django import template

register = template.Library()


@register.filter(name='sum_economic_loss')
def sum_economic_loss(effect_list):
    """Sums the economic loss values in an effects list"""
    return sum(el.economic_loss for el in effect_list)
