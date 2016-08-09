from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

def blog_view(request):
    """The view for your blog page"""
    
    post_list = Post.objects.all().order_by("-date")[:25]
    #post_list = ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25])

    template = loader.get_template('blog/blog.html')
    context = RequestContext(request,{
        'post_list': post_list,
        
    })
    return HttpResponse(template.render(context))
    # return HttpResponse('gdkgshdkgdk')

