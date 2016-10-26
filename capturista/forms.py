from django import forms
from projects.models import Project


class FilesForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['img','anexo']
		labels = {
		'img':'Imagen, relacionada al proyecto (opcional)',
		'anexo':'¿Tienes algún archivo que complemente el proyecto?'
		}