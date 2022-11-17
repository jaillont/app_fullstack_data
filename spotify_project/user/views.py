from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse

from . import forms


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request,
        'user/signup.html',
        context={
            'form': form
        }
    )

def login_page(request):
    form = forms.CustomLoginForm()

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(
        request,
        'user/login.html',
        context={
            'form': form
        }
    )
