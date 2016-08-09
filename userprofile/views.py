from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from userprofile.models import User
from blog.models import Post

# from django.conf.urls import reverse
from django.http import HttpResponseRedirect

def userposts(request):
    """The view for your profile page"""
    
    user = User.objects.all()
    post = Post.objects.all()

    template = loader.get_template('userprofile/userposts.html')
    context = RequestContext(request,{
        'user_lst': user,
        'post_lst': post,
        
    })
    return HttpResponse(template.render(context))


    # template = loader.get_template('userprofile/userprofile.html')
    # context = RequestContext(request,{
    #     'user': user,
        
    # })
    # return HttpResponse(template.render(context))




def login_view(request):
	return render(request, 'userprofile/login.html')
	# template = loader.get_template('userprofile/login.html')
 #    	return HttpResponse(template)

# def register_view(request):
# 	 template = loader.get_template('userprofile/register.html')
    
#     return HttpResponse(template)
