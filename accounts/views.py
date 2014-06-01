from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from accounts.forms import LoginForm, RegisterForm

@csrf_protect
def account_login(request):
	""" Account Login"""
	if request.method == "GET":
		return render(request, 'accounts/login.html', {'form': LoginForm})

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('account_profile')
			else:
				return render(request, 'accounts/login.html', {'form': LoginForm, 'error_message': 'Account is not Active.'})
		else:
			return render(request, 'accounts/login.html', {'form': LoginForm, 'error_message': 'Username and Password Invalid.'})

def account_logout(request):
	""" Account Logout """
	logout(request)
	return redirect('hcub3d_home')

@login_required
def account_profile(request):
	""" Account Profile """
	user = request.user
	return render(request, 'accounts/profile.html', {'user': user})

def account_register(request):
	""" Account Register """
	if request.method == "GET":
		return render(request, 'accounts/register.html', {'form': RegisterForm})

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		# See if username already exists
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		
		# Create username if not already taken
		if user is not None:
			return render(request, 'accounts/register.html', {'form': RegisterForm, 'error_message': 'Username already taken.'})
		else:
			User.objects.create_user(username=username, password=password)
			return redirect('account_login')
            

