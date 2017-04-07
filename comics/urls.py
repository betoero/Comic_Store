from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^list_comics/$', views.ListComics.as_view(), name="list_comics"),
]