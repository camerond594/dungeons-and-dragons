from django.conf.urls import url

from character_sheets import views

urlpatterns = [
    url(r'characters/new/$', views.character_create, name='character_create'),
    url(r'characters/(?P<pk>\d+)/edit/$', views.character_edit, name='character_edit'),
    url(r'characters/(?P<pk>\d+)/$', views.character_detail, name='character_detail'),
    url(r'characters/$', views.character_list, name='character_list'),
    url(r'$', views.character_list, name='character_list'),
    # url(r'$', views.sheets_base, name='sheets_base'),
]