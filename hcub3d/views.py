from django.shortcuts import render

def home(request):
	""" Home """
	user = request.user
	return render(request, 'index.html', {'user': user})