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

	# user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=140,blank=True,null=True)
	# apellido = models.CharField(max_length=140,blank=True,null=True)
	email = models.EmailField(blank=True,null=True)
	edad = models.CharField(max_length=140 ,blank=True,null=True)
	displayName = models.CharField(max_length=140,blank=True,null=True)
	photoURL = models.CharField(max_length=140,blank=True,null=True)
	ocupacion = models.CharField(max_length=140,blank=True,null=True)
	telefono = models.CharField(max_length=140,blank=True,null=True)
	uid = models.CharField(max_length=140,blank=True,null=True)
	password = models.CharField(max_length=140,blank=True,null=True)

	def __str__(self):
		return 'email: {}, UID: {}'.format(self.email,self.uid)
