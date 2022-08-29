from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404
from .models import Tutorial, Visite
from django.urls import path
from .models import Category
from user.models import Profile
from django.conf import settings
#from blog.models import Comment
from django.views.decorators.http import condition
from django.core import serializers
#User
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
import datetime
#from django.http import urllib

import os


def getLink(title):
    template = tutorial.title.replace(" ", "_").lower()+".html"
    return template


def tutorial_detail(request, slug=""):
    print("slug"+str(slug)+"base dir ==="+settings.BASE_DIR)
    arguments = False
    author_tutorial = ''
    users = []
    tutorial_all = Tutorial.objects.all()
    categorie = Category.objects.all()
    try:
        for tutorial in tutorial_all:
            author_tutorial = str(tutorial.author)
            profile = Profile.objects.get(first_name=author_tutorial)
            if profile not in users:
                users.append(profile)
    except Exception:
        print('Problema nel creare la lista autori dei tutorial')
    if arguments is True:
        try:
            print("TRY per prendere tutorial ok ! arguments="+str(arguments))
            tutorial = Tutorial.objects.get(
                publish__year=year, slug=slug)
        except UnboundLocalError:
            print("ECCEZIONE : prendo l' ultimo tutorial scritto! ")
            tutorial = Tutorial.objects.latest('publish')
    try:
        user = tutorial.author
    except UnboundLocalError:
        return HttpResponse("Non ci sono Pagine ")
    print("user= "+str(user))
    autore = str(user)
    photo = settings.MEDIA_URL+str(user.photo)
    mypath = str(request.path).replace("/", "")
    if not mypath:
        print("request PATH VUOTA"+mypath)
        tutorial = Tutorial.objects.latest('publish')
    else:
        print("request PATH PIENA"+mypath)
        try:
            tutorial = Tutorial.objects.get(slug=slug)
        except:
            print("WARNING ! non ci sono tutorial nel database ! ")
        print("request PAth piena e Tutorial"+str(tutorial.slug))
    template = tutorial.slug+".html"
    try:
        user = tutorial.author
    except UnboundLocalError:
        return HttpResponse("Non ci sono Pagine ")
    autore = str(user)
    photo = settings.MEDIA_URL+str(user.photo)
    print("Requestpath & template="+str(request.path+template))
    vis = Visite()
    try:
        lastobj = Visite.objects.latest('visite')
        vis.visite = lastobj.visite+1
    except Exception:
        vis.visite = 1
    vis.save()
    return render(request, template, {'tutorial': tutorial, 'visitato':
                                      vis, 'login': request.user.is_authenticated,
                                      'tutorial_all': tutorial_all, 'categorie': categorie,
                                      'photo': photo, 'users': users, 'autore':
                                      autore})


def readInfoClient(request):
    req = request.META['HTTP_USER_AGENT']
    return str(req)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
