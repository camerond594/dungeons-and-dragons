from django.conf.urls import include
from django.conf.urls import url

from character_sheets import views

urlpatterns = [
    url(r'^', views.home_page),
]