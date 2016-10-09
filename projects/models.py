from django.db import models
from django.conf import settings


class Category(models.Model):
	name = models.CharField(max_length=140)
	# projects = models.ManyToManyField(Project, related_name='categories')

	def __str__(self):
		return self.name


class Project(models.Model):
	""" Modelo para Projecto en Base de datos """
	title = models.CharField(max_length=140)
	slug = models.SlugField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects')
	img = models.ImageField(blank=True,null=True,upload_to="projects/%Y/%m/%d/images")
	desc = models.TextField(blank=True,null=True)
	votes = models.IntegerField(default=0)
	categories = models.ManyToManyField(Category,related_name='projects')

	def __str__(self):
		return self.title


class Comment(models.Model):
	""" Modelo para review en base de datos """
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
	project = models.ForeignKey(Project, related_name='reviews')
	comment = models.TextField()

	def __str__(self):
		return "{} review {}".format(self.user,self.project)





