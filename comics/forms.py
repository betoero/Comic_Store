from django import forms
from .models import Comic, Company, Category

CATEGORY_CHOICES = (('DC Comics', 'dc'), ('Marvel', 'marvel'))

class ComicForm(forms.ModelForm):
	class Meta: 
		model =  Comic
		fields = ('title','company', 'category', 'image', 'price', 'description', 'author', 'date', 'slug')

class CategoryForm(forms.Form):
		category = forms.ChoiceField(choices=CATEGORY_CHOICES)
		fields = ('category',)