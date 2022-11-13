from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(
        request,
        'playlists/home.html',
        context={}
    )

@login_required
def playlists(request):
    return HttpResponse('<h1>Here we are cretaing the playlist page !</h1>')