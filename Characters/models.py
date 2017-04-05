from django.db import models

# Create your models here.

class Universe(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	description = models.TextField()
	image = models.ImageField(upload_to = 'universo',blank=True)

# class Bando(models.Model):
# 	name = models.CharField(max_length=200, db_index=True)
# 	slug = models.SlugField(max_length=200, db_index=True)

class Personaje(models.Model):
	# Bando = models.ManyToManyField((Bando, related_name='bando'))
	alias = models.CharField(max_length=200, db_index=True)
	powers = models.SlugField(max_length=200, db_index=True) 
	occupation = models.TextField() 
	first_appearance = models.CharField(max_length=200)
	real_name = models.CharField(max_length=200) 
	image = models.ImageField(upload_to = 'personajes',blank=True) 
	description = models.TextField()