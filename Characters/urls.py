from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^heroes-and-villains/$', views.ComicsUniverse.as_view(), name = "heroes-and-villains"),
]