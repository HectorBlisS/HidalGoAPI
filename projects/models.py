from django.db import models
from django.conf import settings


class CategoryManager(models.Manager):
	def get_by_natural_key(self, name,id):
		return self.get(id=id,name=name)

class ProjectManager(models.Manager):
	def get_by_natural_key(self, name,title):
		return self.get(id=id,name=title)

class Category(models.Model):
	name = models.CharField(max_length=140)
	# projects = models.ManyToManyField(Project, related_name='categories')

	def __str__(self):
		return self.name

	def natural_key(self):
		return (self.id, self.name)

	class Meta:
		unique_together = (('name', 'id'),)


class Project(models.Model):
	""" Modelo para Projecto en Base de datos """
	title = models.CharField(max_length=140)
	uid = models.CharField(max_length=140,blank=True,null=True)
	eje = models.CharField(max_length=140,null=True,blank=True)
	slug = models.SlugField(blank=True,null=True)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects',blank=True,null=True)
	img = models.ImageField(blank=True,null=True,upload_to="projects/%Y/%m/%d/images")
	imagen = models.CharField(max_length=500 ,blank=True,null=True)
	objetivo_general = models.TextField(blank=True,null=True)
	indicador = models.CharField(max_length=140,blank=True,null=True)
	planteamiento = models.TextField(blank=True,null=True)
	problematica = models.TextField(blank=True,null=True)
	municipio = models.CharField(max_length=140,blank=True,null=True)
	votes = models.IntegerField(default=0)
	categories = models.ManyToManyField(Category,related_name='projects',blank=True,null=True)
	anexo = models.FileField(blank=True,null=True)
	cerrado = models.BooleanField(default=False)

	
	def __str__(self):
		return self.title

	def natural_key(self):
		return (self.id, self.title)

	class Meta:
		unique_together = (('title', 'id'),)


class Comment(models.Model):
	""" Modelo para review en base de datos """

	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
	project = models.ForeignKey(Project, related_name='reviews')
	comment = models.TextField()

	def __str__(self):
		return "{} review {}".format(self.user,self.project)





