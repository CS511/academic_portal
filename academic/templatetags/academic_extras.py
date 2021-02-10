from django import template

register = template.Library()

@register.filter(is_safe=True)
def sum_total_credits(group_list):
   return sum(d.get('credits') for d in group_list)
