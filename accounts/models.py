from django.db import models
from django.conf import settings
from projects.models import Project


class Profile(models.Model):

	TIPOS_USERS = (
			('ciudadano','Ciudadano'),
			('estudiante','Estudiante'),
			('empresario','Empresario'),
			('docente','Docente'),
		)

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=140,blank=True,null=True)
	apellido = models.CharField(max_length=140,blank=True,null=True)
	email = models.EmailField(blank=True,null=True)
	dir = models.CharField(max_length=140,blank=True,null=True)
	displayName = models.CharField(max_length=140,blank=True,null=True)
	photoURL = models.CharField(max_length=140,blank=True,null=True)
	tipo = models.CharField(max_length=140,choices=TIPOS_USERS,default="ciudadano",blank=True,null=True)
