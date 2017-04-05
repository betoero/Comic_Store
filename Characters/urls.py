from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^heroes_and_villains/$', views.HeroesAndVillains.as_view(), name = "heroes-and-villains"),
]