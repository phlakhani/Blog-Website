from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserRegisterform(UserCreationForm):
	email= forms.EmailField()   # required  in Emailfield bydefault true
	city= forms.CharField()


	class Meta:     # meta class used to see representation in form
		model= User                        # it shows model that we gonna use in form   here User model is default model of
		fields=['username','email','city','password1','password2']  # it shows this many fields(of that above model) will be there in form


#following class are used to update user info like username, email & profile pic

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model= User           # name of model     here User is default model of django
		fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model= profile   # name of model
		fields=['image']   # field of that models that needs to be changes