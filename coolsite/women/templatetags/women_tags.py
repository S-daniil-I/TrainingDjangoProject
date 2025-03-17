from django import template
from women.models import *

register = template.Library()

# @register.simple_tag()
# def get_categories():
#     return Category.objects.all()

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_select):
    categories = Category.objects.all()
    return {'categories': categories, 'cat_selected': cat_select}

@register.inclusion_tag('women/list_menu.html')
def get_menu():
    return {'menu': menu}