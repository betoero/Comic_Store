from django.shortcuts import render
from django.views.generic import View
from.models import Category, Company, Comic
from django.utils.decorators import method_decorator


# Create your views here.
class ListComics(View):
	def get(self, request, category_slug=None, company_slug=None):
		template_name = "comics/list_comics.html"
		categories = Category.objects.all()
		comics = Comic.objects.all()
		company = Company.objects.all()
		if category_slug:
			category = get_object_or_404(Category, slug=category_slug)
			comics = comics.filter(category = category)
		if company_slug:
			company = get_object_or_404(Company, slug=company_slug)
			comics = comics.filter(category =  category)
		context = {
			'comics':comics,
			'categories':categories,
			'company':company,
		}
		return render(request, template_name, context)