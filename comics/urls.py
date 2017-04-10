from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^list_comics/$', views.ListComics.as_view(), name="list_comics"),
	url(r'^new_comic/$', views.NewComic.as_view(), name="new_comic"),
	url(r'^(?P<category_slug>[-\w]+)/$', views.ListComics.as_view(), name="comics_list_category"),
	url(r'^(?P<company_slug>[-\w]+)/$', views.ListComics.as_view(), name="comics_list_company"),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.DetailComics.as_view(), name="detail_comics"),
]