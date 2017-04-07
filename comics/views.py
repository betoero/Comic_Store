from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from.models import Category, Company, Comic
from django.utils.decorators import method_decorator


# Create your views here.
class ListComics(View):
	def get(self, request, category_slug=None, company_slug=None):
		template_name = "comics/list_comics.html"
		category = None
		company = None
		categories = Category.objects.all()
		comics = Comic.objects.all()
		company = Company.objects.all()
		if category_slug:
			category = get_object_or_404(Category, slug=category_slug)
			comics = comics.filter(category = category)
		if company_slug:
			company = get_object_or_404(Company, slug=company_slug)
			comics = comics.filter(company = company)
		context = {
			'category':category,
			'comics':comics,
			'categories':categories,
			'company':company,
		}
		return render(request, template_name, context)

class DetailComics(View):
	def get (self, request, id, slug):
		template_name = "comics/detail_comics.html"
		comics = get_object_or_404(Comic, id=id, slug=slug)
		company = Company.objects.all()
		categories = Category.objects.all()
		context = {
			'comics':comics,
			'categories': categories, 
			'company':company,
		}
		return render(request, template_name, context)