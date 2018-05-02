from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf.urls import include, url
from django.views.generic import View, ListView, DetailView
from userprofile.models import User
from blog.models import Post

from django.contrib import messages
import datetime

# from userprofile.forms import UserForm
from django.contrib.auth import authenticate, login

# from django.conf.urls import reverse
from django.http import HttpResponseRedirect

def userposts(request):
    username = ""
    loggedin = "1"
    
    if 'u_id' in request.session:
        loggedin = "1"
        username = request.session['u_id']
    else:
        loggedin = "0"

    user = User.objects.all()
    post = Post.objects.all()

    template = loader.get_template('userprofile/userposts.html')
    context = RequestContext(request,{
        'user_lst': user,
        'post_lst': post,
        'loggedin': loggedin,
        'username': username,
        
    })
    return HttpResponse(template.render(context))


    # template = loader.get_template('userprofile/userprofile.html')
    # context = RequestContext(request,{
    #     'user': user,
        
    # })
    # return HttpResponse(template.render(context))

def pkposts(request, pk):
    user = User.objects.get(id=pk)
    # usrname = user.user_name
    post = Post.objects.filter(user_name_id=pk)
    # post = Post.objects.all()


    username = ""
    loggedin = "1"
    
    if 'u_id' in request.session:
        loggedin = "1"
        username = request.session['u_id']
    else:
        loggedin = "0"


    template = loader.get_template('userprofile/pkposts.html')
    context = RequestContext(request,{
        'user_lst': user,
        'post_lst': post,
        'loggedin': loggedin,
        'username': username,
        
    })
    return HttpResponse(template.render(context), pk)
    # return render_to_response('userprofile/pkposts.html')

def users(request):
    username = ""
    loggedin = "1"
    
    if 'u_id' in request.session:
        loggedin = "1"
        username = request.session['u_id']
    else:
        loggedin = "0"

    user = User.objects.all()
    template = loader.get_template('userprofile/users.html')
    context = RequestContext(request,{
        'user_lst': user,
        'loggedin': loggedin,
        'username': username,
    })
    return HttpResponse(template.render(context))

def register_view(request):
    if 'u_id' in request.session:
        return HttpResponseRedirect('dashboard')
    else:  
        if request.method == 'POST':
            if 'rusername' in request.POST and 'rpassword' in request.POST and 'rname' in request.POST and 'rcpassword' in request.POST:
                username = request.POST['rusername']
                password = request.POST['rpassword']
                name = request.POST['rname']
                cpassword = request.POST['rcpassword']

                if cpassword == password:
                    userinstance = User()
                    userinstance.fname = name
                    userinstance.user_name = username
                    userinstance.password = password
                    userinstance.save()

                    messages.success(request, 'You are registered. Now login.')
                    return HttpResponseRedirect('login')
                    
                else:
                    messages.error(request, "Passwords don't match!")
                    return HttpResponseRedirect('register')
            else:
                return render(request, 'userprofile/register.html')
        else:
            username = ""
            loggedin = "1"
    
            if 'u_id' in request.session:
                loggedin = "1"
                username = request.session['u_id']
            else:
                loggedin = "0"
            
            ctx = {
                'username': username,
                'loggedin': loggedin,
            }
            return render(request, 'userprofile/register.html', ctx)
	

def login_view(request):
    if 'u_id' in request.session:
        return HttpResponseRedirect('dashboard')
    else:
        if request.method == 'POST':
            if 'lusername' in request.POST and 'lpassword' in request.POST:
                username = request.POST['lusername']
                password = request.POST['lpassword']

                if User.objects.filter(user_name=username).exists():
                    user = User.objects.get(user_name=username)
                    pw = user.password
                    if pw == password:
                        request.session['u_id'] = user.user_name
                        
                        return HttpResponseRedirect('dashboard')
                        # return render(request, 'userprofile/userdashboard.html', {"username": user.user_name})

                        # return HttpResponseRedirect('/blog')
                    else:
                        messages.error(request, "You forgot your password, " + user.user_name)
                        return HttpResponseRedirect('login')
                else:
                    messages.error(request, "User doesn't exist! Register maybe?")
                    return HttpResponseRedirect('register')

            else:
                return render(request, 'userprofile/register.html')

        else:
            username = ""
            loggedin = "1"
    
            if 'u_id' in request.session:
                loggedin = "1"
                username = request.session['u_id']
            else:
                loggedin = "0"
            ctx = {
                'username': username,
                'loggedin': loggedin,
            }
            return render(request, 'userprofile/login.html', ctx)

def dashboard_view(request):
    if 'u_id' not in request.session:
        messages.error(request, "You must be logged in!")
        return HttpResponseRedirect('login')
    else:
        username = request.session['u_id']
    
    if request.method == 'POST':
        title = request.POST['ptitle']
        body = request.POST['pbody']
        dt = str(datetime.datetime.now())
        print(dt)
        post = Post()

        post.user_name = User.objects.get(user_name=username)
        post.title = title
        post.body = body
        post.date = dt

        post.save()
        return HttpResponseRedirect('/blog')
        
    else:
       return render(request, 'userprofile/userdashboard.html', {"username": username})


def logout_view(request):
    if 'u_id' in request.session:
        del request.session['u_id']
        messages.success(request, 'Logged out. Login again?')
        return HttpResponseRedirect('login')
    else:
        messages.success(request, 'Already logged out.')
        return HttpResponseRedirect('/')








