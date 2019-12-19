from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.contrib import admin
# Create your views here.

def list_name(request):
    profiles=Profile.objects.all()
    return render (request, 'myprofile/list_name.html',{'profiles':profiles})


def detail(request,profile_id):
    profile=get_object_or_404(Profile, pk=profile_id) 
    return render(request, 'myprofile/detail.html',{'profile':profile})
