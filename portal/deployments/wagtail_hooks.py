from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import wordpress,saas


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('deployments/wordpress/', wordpress, name='wordpress'),
        path('deployments/saas/', saas, name='saas'),
    ]



@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    submenu = Menu(items=[
        MenuItem('Wordpress', reverse('wordpress'), icon_name='globe'),
        MenuItem('SAAS', reverse('saas'), icon_name='globe'),
    ])

    return SubmenuMenuItem('Deployments', submenu, icon_name='globe')