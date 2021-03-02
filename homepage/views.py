from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404
from .models import Tutorial,Visite
from django.urls import path
from .models import Category
from user.models import Profile
from django.conf import settings
from blog.models import Comment
#User
from django.contrib.auth.models import User
import datetime
#from django.http import urllib

import os



def getLink(title):
    template=tutorial.title.replace(" ","_").lower()+".html"
    return template

def tutorial_detail(request, **kwargs):
    users=[]
    arguments=False
    user_string=''
    author_tutorial=''
    print("entry in tutorial_detail view Kwargs="+str(kwargs.items()))
    if request.user.is_authenticated:
        login=True
    else:
        login=False
    tutorial_all = Tutorial.objects.all()
    categorie=Category.objects.all()
    #prendo user di cui esiste almeno un tutorial, per creare il leftmenu
    for tutorial in tutorial_all:
        print("Tutorial author"+str(tutorial.author))
        author_tutorial=str(tutorial.author).replace(" ","")
        for profile in Profile.objects.all():
            user_string=str(profile.first_name)
            user_string=user_string.replace(" ","")
            if user_string==author_tutorial:
                print("USER del Tutorial"+"mario")
                if not profile in users:
                    try:
                        users.append(profile)
                        print("APPESO PROFILE IN USERS="+str(users))
                    except UnboundLocalError:
                        print ("error add profile in user's list")
        tutorials_user=users
        print("Users CON ALMENO U NN TUTORIAL:"+str(tutorials_user))
    #users=Profile.objects.all()
    try:
     for key,value in kwargs.items():
        arguments=True
        if 'year' in str(key) :
            year=str(value)
            print("year="+year)
        elif 'month' in key:
            month=str(value)
            print("moth="+month)
        elif 'day' in key:
            day=str(value)
            print("day="+day)
        elif 'post' in key:
            slug=str(value)
            print("slug="+slug)
        else :
            print ("No KEY OR VALUE IN KWARGS !")
    except: "Eccezione NEL RECUPERO  di KEY E VALUE"
    if arguments is True:
        try:
            print("TRY per prendere tutorial ok ! arguments="+str(arguments))
            tutorial = Tutorial.objects.get(
            publish__year=year,slug=slug)
        except UnboundLocalError :
            print("ECCEZIONE : prendo l' ultimo tutorial scritto! ")
            tutorial=Tutorial.objects.latest('publish')
    user=tutorial.author
    autore=str(user)
    photo=settings.MEDIA_URL+str(user.photo)
    #photo=user.photo
    #print("anno?="+str(tutorial.publish.year)+str(tutorial.publish.day)+"autor="+str(tutorial.author)+"photo="+str(photo))
    #print("COMMENTI="+str(tutorial.all_comments.all()))

    if not request.path:
        print("request PATH VUOTA")
        tutorial=Tutorial.objects.latest('publish')
        user=tutorial.author
        autore=str(user)
        photo=settings.MEDIA_URL+str(user.photo)
    template=tutorial.slug.replace(" ","_").lower()+".html"
    print("Requestpath & template="+str(request.path+template))
    vis=Visite()
    try:
        lastobj=Visite.objects.latest('visite')
        vis.visite=lastobj.visite+1
    except :
        vis.visite=1
    vis.save()
    return render(request,template,{'tutorial': tutorial,'visitato':vis,'login':login,'tutorial_all':tutorial_all,'categorie':categorie,'photo':photo,'users':users,'autore':autore})

def readInfoClient(request):
    req=request.META['HTTP_USER_AGENT']
    return str(req)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
