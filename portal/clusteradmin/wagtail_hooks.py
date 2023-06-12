from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import onpremise,aws


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('clsuteradmin/on-prem/', onpremise, name='on-premise'),
        path('clsuteradmin/aws/', aws, name='aws'),
    ]



@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    submenu = Menu(items=[
        MenuItem('On-Premise', reverse('on-premise'), icon_name='globe'),
        MenuItem('AWS', reverse('aws'), icon_name='globe'),
    ])

    return SubmenuMenuItem('Cluster Admin', submenu, icon_name='globe')