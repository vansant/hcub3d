from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def account_login(request):
	""" Account Login"""
	if request.method == "GET":
		return render(request, 'accounts/login.html')

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('account_profile')
			else:
				return render(request, 'accounts/login.html', {'error_message': 'Account is not Active.'})
		else:
			return render(request, 'accounts/login.html', {'error_message': 'Username and Password Invalid.'})

def account_logout(request):
	""" Account Logout """
	logout(request)
	return redirect('hcub3d_home')

@login_required
def account_profile(request):
	""" Account Profile """
	user = request.user
	return render(request, 'accounts/profile.html', {'user': user})

@csrf_protect
def account_register(request):
	""" Account Register """
	if request.method == "GET":
		return render(request, 'accounts/register.html')

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
				
		# Require username and password
		if not username or not password:
			return render(request, 'accounts/register.html', {'error_message': 'Username and Password required.'})

		# See if username already exists
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		
		# Create username if not already taken
		if user is not None:
			return render(request, 'accounts/register.html', {'error_message': 'Username already taken.'})
		else:
			User.objects.create_user(username=username, password=password)
			return redirect('account_register_success')
            
def account_register_success(request):
	return render(request, 'accounts/success.html')
