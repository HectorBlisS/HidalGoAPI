from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['title','uid','eje','img','objetivo_general','indicador','planteamiento','municipio','problematica','imagen','laRef','archivo','fileRef','cerrado']


