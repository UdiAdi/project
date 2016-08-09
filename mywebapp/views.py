from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'mywebapp/home.html')

def contact(request):
	return render(request, 'mywebapp/contact.html', {'content' : ['Contact me at this email', 'abc@gmail.com']})