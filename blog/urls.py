from django.shortcuts import get_object_or_404
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views


urlpatterns = [
	#/blog/
    url(r'^$', views.blog_view, name="blogg"),

    #/blog/1/
    url (r'^(?P<pk>\d+)/$', DetailView.as_view(model=Post, template_name='blog/post.html'), name="detail"),
   ]
