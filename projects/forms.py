from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
	correo = forms.EmailField()
	contrasena = forms.CharField(widget=forms.PasswordInput)
	contrasena_again = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Project
		fields = ['title','correo','contrasena','contrasena_again','uid','eje','img','objetivo_general','indicador','planteamiento','municipio','problematica','imagen','laRef','archivo','fileRef','cerrado']

	def clean_contrasena_again(self):
		cd = self.cleaned_data
		if cd['contrasena'] != cd['contrasena_again']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['contrasena_again']

