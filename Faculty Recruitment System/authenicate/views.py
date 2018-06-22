from __future__ import unicode_literals
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import User
from django.template.context_processors import csrf


# Create your views here.
def signin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('signin.html', c)


def validate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/welcome/dashboard')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def invalid(request):
    return render_to_response('invalid.html')


def signup(request):
    args = {}
    args.update(csrf(request))
    return render(request, 'signup.html', args)


def create(request):
    # firstname = request.POST.get('firstname','')
    # lastname = request.POST.get('lastname','')
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    # email = request.POST.get('email','')
    if username and password1 and (password1 == password2):
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect('/profile/create')
    else:
        return HttpResponseRedirect('/accounts/error/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/index")
