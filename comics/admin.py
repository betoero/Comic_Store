from django.contrib import admin
from .models import Company, Category, Comic
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',),}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',),}

class ComicAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'date', 'autor', 'price']
	prepopulated_fields = {'slug':('title',),}

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comic, ComicAdmin)
