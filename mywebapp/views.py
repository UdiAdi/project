from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
	ctx = {}
	if 'u_id' in request.session:
 		ctx = {
 		'loggedin': "1",
 		'username': request.session['u_id'],
 		}
 	else:
 		ctx = {
 		'loggedin': "0",
 		}
	return render(request, 'mywebapp/home.html', context = ctx)

def contact(request):
	ctx = {}
	if 'u_id' in request.session:
 		ctx = {
 		'loggedin': "1",
 		'username': request.session['u_id'],
 		'content' : ['Contact me at this email', 'abc@gmail.com']
 		}
 	else:
 		ctx = {
 		'loggedin': "0",
 		'content' : ['Contact me at this email', 'abc@gmail.com']
 		}
	return render(request, 'mywebapp/contact.html', ctx)

