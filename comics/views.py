from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class ListComics(View):
	def get(self, request):
		template_name = "comics/list_comics.html"
		context = {

		}