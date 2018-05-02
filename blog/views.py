from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

def blog_view(request):
    
	post_list = Post.objects.all().order_by("-date")[:25]

	template = loader.get_template('blog/blog.html')

	username = ""
	loggedin = "1"
    
	if 'u_id' in request.session:
		loggedin = "1"
		username = request.session['u_id']
	else:
		loggedin = "0"
	
	context = RequestContext(request,{
		'post_list': post_list,
        'loggedin': loggedin,
        'username': username,
    })

	return HttpResponse(template.render(context))