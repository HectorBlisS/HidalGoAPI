from django import forms
from .models import Project, Conclusion
from account.models import Profile


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['title','uid','eje','img','objetivo_general','indicador','planteamiento','municipio','problematica','imagen','laRef','anexo','fileRef','cerrado','alcance','foro','conclusiones']


class ProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'required':'true'}))
	password_again = forms.CharField(widget=forms.PasswordInput(attrs={'required':'true'}))
	class Meta:
		model = Profile
		fields = ['email','password']

	def clean_password_again(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password_again']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password_again']
		

class EditProyectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = [
			'title',
			# 'uid',
			'user',
			'eje',
			'objetivo_general',
			'indicador',
			'planteamiento',
			'municipio',
			'problematica',
			'alcance',
			'foro',
			'img',
			# 'imagen',
			'anexo',
			'autor_name',
			'autor_tel',
			'autor_correo',
			'conclusiones'

		]
		labels = {
		'title':'Titulo del proyecto',
		'user':'Capturista del proyecto',
		'img':'Imagen',
		'foro':'Foro presencial',
		'autor_name':'Nombre del autor',
		'autel_tel':'Teléfono del autor',
		'autor_correo':'Correo del autor'
		}


class ConclusionForm(forms.ModelForm):
	class Meta:
		model = Conclusion
		fields = [
			'nombre',
			'foro',
			'otro',
			'conclusion'
		]
		labels = {
		'nombre':'Nombre completo de quien redacta la conclusión',
		'foro':'Selecciona el foro al que corresponde la conclusión',
		'otro':'Escribe el nombre del nuevo foro si es el caso',
		'conclusion':'Escribe tus conclusiones'
		}
