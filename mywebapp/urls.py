from django.conf.urls import include, url
from . import views

# app_name = 'mywebapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
]
