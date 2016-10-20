from django import forms
from .models import Profile


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
			'uid',
			'name',
			'email',
			'edad',
			'ocupacion',
			'telefono'
		]
