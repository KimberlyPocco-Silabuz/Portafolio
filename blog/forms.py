from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(
	label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k: "" for k in fields}


class ProjectForm(forms.ModelForm):
	url_imagen = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'url imagen'}), required=True)
	titulo = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'título del proyecto'}), required=True)
	descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'descripción del proyecto'}), required=True)

	class Meta:
		model = Project
		fields = ['url_imagen','titulo','descripcion']
