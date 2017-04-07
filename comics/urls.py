from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^list_comics/$', views.ListComics.as_view(), name="list_comics"),
	url(r'^(?P<category_slug>[-\w]+)/$', views.ListComics.as_view(), name="comics_list_category"),
	url(r'^(?P<company_slug>[-\w]+)/$', views.ListComics.as_view(), name="comics_list_company"),
]