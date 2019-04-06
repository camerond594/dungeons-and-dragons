from django.conf.urls import url

from character_sheets import views

urlpatterns = [
    url(r'$', views.character_list, name='character_list'),
    url(r'characters/$', views.character_list, name='character_list'),
    url(r'characters/new/$', views.character_create, name='character_create'),
]