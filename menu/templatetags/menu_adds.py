from django import template
from menu.models import Branch
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(Branch, title=menu_name, parent=None)
    local_context = {'menu_item': menu}
    requested_url = context['request'].path
    try:
        active_menu_item = Branch.objects.get(title=requested_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = active_menu_item.get_elder_ids() + [active_menu_item.id]
        local_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids
    return local_context

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    menu_item = get_object_or_404(Branch, pk=menu_item_id)
    local_context = {'menu_item': menu_item}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']
    return local_context