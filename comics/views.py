from django.shortcuts import render
from django.views.generic import View
from.models import Category, Company, Comic

# Create your views here.
class ListComics(View):
	def get(self, request):
		template_name = "comics/list_comics.html"
		categories = Category.objects.all()
		comics = Comic.objects.all()
		context = {
			'comics':comics,
			'categories':categories,
		}
		return render(request, template_name, context)