from __future__ import unicode_literals

from django.conf.urls import url

from character_sheets import views

urlpatterns = [

    url(r'^characters/create/$', views.create_character, name='create_character'),
    url(r'^edit/$', views.list_edit_characters, name="list_edit_characters"),
    url(r'^characters/$', views.list_characters, name="list_characters"),
    url(r'^characters/(?P<character_id>\d+)/$', views.character_detail, name="character_detail"),
    url(r'^characters/(?P<character_id>\d+)/edit/$', views.character_edit, name="character_edit"),
]