from __future__ import unicode_literals

from django.conf.urls import url

from character_sheets import views

urlpatterns = [

    url(r'^create/$', views.create_character, name='create_character'),
    url(r'^edit/$', views.list_edit_characters, name="list_edit_characters"),
    url(r'^view_all/$', views.get_characters, name="get_characters"),
]