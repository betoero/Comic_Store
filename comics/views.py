from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from.models import Category, Company, Comic
from django.utils.decorators import method_decorator
from .forms import ComicForm, CategoryForm


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

class NewComic(View):
	def post(self, request):
		template_name = 'comics/new_comic.html'
		comic_form = ComicForm(request.POST, request.FILES)
		comic_form_list = ComicForm()
		if comic_form.is_valid():
			new_comic = comic_form.save(commit=False)
			new_comic.user_movie = request.user
			new_movie.save()
			return redirect('comics:list_comics')
		else:
			context = {
				'comic_form_list':comic_form_list, 

			}
		return render(request, template_name, context)

	def get (self, request):
		template_name = 'comics/new_comic.html'
		comic_form = ComicForm()
		category_form = CategoryForm()
		context = {
			'comic_form':comic_form,
			'category_form':category_form,
		}
		return render (request, template_name, context)



# class NewMovie(View):
# 	def post (self, request):
# 		template_name = 'catalogo/new-movie.html'
# 		movie_form = MovieForm(request.POST, request.FILES)
# 		movie_form_list =  MovieForm()
# 		if movie_form.is_valid():
# 			new_movie = movie_form.save(commit=False)
# 			new_movie.user_movie = request.user
# 			new_movie.save()
# 			return redirect('catalogo:list-movies')
# 		else:
# 			context = {
# 				'movie_form_list': movie_form_list,
# 			}
# 		return render (request, template_name, context)

# 	def get (self, request):
# 		template_name = 'catalogo/new-movie.html'
# 		movie_form = MovieForm()
# 		context = {
# 			'movie_form':movie_form, 
# 		}
# 		return render(request, template_name, context)