from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	description = models.CharField(max_length=400)

	class Meta:
		ordering=('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('comics:comics_list_company', args=[self.slug])
	


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	description = models.CharField(max_length=200)

	class Meta:
		ordering=('name',)
		verbose_name='category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('comics:comics_list_category', args=[self.slug])

class Comic(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	company = models.ForeignKey(Company, related_name='company_comic', blank=True)
	category = models.ForeignKey(Category, related_name='category_comic', blank=True)
	slug = models.SlugField(max_length=200)
	date = models.DateField(blank = True, null = True)
	image = models.ImageField(upload_to='comics/%Y/%m/%d', blank=True)
	author = models.CharField(max_length=100, db_index=True)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	description = models.CharField(max_length=1000, db_index=True, blank=True)

	class Meta:
		ordering=('title',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('comics:detail_comics', args=[self.id, self.slug])


