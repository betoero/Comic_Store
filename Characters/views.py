from django.shortcuts import render
from .models import Universe
from django.views.generic import View

# Create your views here.

class ComicsUniverse(View):
	def get(self, request):
		template_name = "characters/comics-universe.html"
		universe = None
		universes = Univerese.objects.all()
		personajes =Personaje.objects.all()

		context = {
			'universe':universe,
			'universes':universes,
			'personajes':personajes,
		}
		return render(request,template_name,context)	