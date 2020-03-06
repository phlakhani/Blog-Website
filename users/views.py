from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from .forms import UserRegisterform, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def registration(request):

	if request.method=='POST':
		form=UserRegisterform(request.POST)
		if form.is_valid():
			#form.save(commit=False)
			username=form.cleaned_data.get('username')
			city=form.cleaned_data.get('city')
			messages.success(request, f'Cheers!! Account successfully created for { username } from { city } ')
			form.save()
			return redirect('loginpage')
	else:
		form=UserRegisterform()
	return render(request,'registrationform.html',{'form':form})


@login_required
def profile(request):
	if request.method=="POST":

		u_form=UserUpdateForm(request.POST, instance=request.user)
		p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, 'Your Profile has been Updated')
				return redirect('profilepage')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


	context={
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request, 'profile.html', context)

