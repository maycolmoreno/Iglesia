# -*- coding: utf-8 -*-

from django import forms
from .models import Registrado
from .models import Reserva
from .models import Persona
from django.core.mail import send_mail
from django.contrib.auth.models import User



class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utiliza un email con la extension .EDU")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)


# Forms registration

class UserForm(forms.ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model = User
		fields = [	
					'id',
					'username', 
					'password', 
					'email'
				]
		labels = { 	'username': 'Usuario',
					'password': 'Contraseña',
					'email': 'Correo electronico',
		}
		widgets = {	
					'id': forms.HiddenInput(),
					'password': forms.PasswordInput(),
					}

class PersonaForm(forms.ModelForm):
	"""docstring for PersonaForm"""
	class Meta:
		model = Persona
		fields = [	
					'id_persona',
					'cedula',
					'nombre',
					'apellido', 
					'direccion',
					'telefono'
				]
		widgets = {
					'id_persona': forms.HiddenInput(),
					
					}


	