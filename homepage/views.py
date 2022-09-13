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


class initHome(View):

    def get(self, request):
        page = """<!DOCTYPE html>
        <html lang="it" id="page" >
        <head>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta charset="UTF-8">
          <meta name="author" content="silverania">
          <meta name="keywords" content="software, webtalk ,hosting, messaggi,commenti,blog,gratuito,addon,sito,web,modulo,download,free,gratis,webmaster,sviluppatori">
          <meta name="description" content="Software Gratuito Per Aggiungere Commenti Sul Tuo Sito Web.">
          <title>Host-WebTalk</title>
          <link rel="icon" type="image/x-icon" href="/static/images/favicon.ico">
          <link rel="stylesheet" href="/static/css/reset.css">
          <link rel="stylesheet" href="/static/css/bootstrap.min.css">
             <link rel="stylesheet" href="/static/css/style.css">
            <script  src="/static/js/jquery.min.js"></script>
            <script  src="/static/node_modules/popper.js/dist/umd/popper.min.js"></script>
          <script  src="/static/js/bootstrap.min.js"></script>
        <script src="/static/js/all.min.js"></script>
        <script src="/static/js/progressbar.js"></script>
        </head>
        <body id="body"  onscroll="var h=document.body.scrollHeight;getPosition();">
            <header><div class="container">
                    <div id="id_row_title" class="row justify-content-center">
                    <div class="col-4">
                        </div>
                    <div class="col-6">
                    <div id="id_div_title" class="class_div_title">
        <h1>Host-WebTalk</h1></div></div>

                        <div class="col-2"> </div>
                </div>

        <div class="row justify-content-center">

        <div id="div_col_info" class="col-5">
        <div id="id_div_info" class="">
        <p class="p_info" id="p_info">Cos'è Host-WebTalk ?</p>
<p id="p_content" class="p_content">Host-WebTalk è un "software libero" di commenti su siti web .   </p>

<p class="p_info" id="p_info">A Chi Può servire ?</p>
<p id="p_content" class="p_content">A chiunque sviluppi siti Web.</p>
<p class="p_info" id="p_info">Installazione</p>
<p id="p_content" class="p_content">Registrati <a href="https://breakingweb.site/user/register/blog">qui</a>
per usare e installare il programma ed avere accesso alla pagina di gestione e moderazione dei messaggi.
Dopodichè nel codice html del tuo sito , copia e incolla i tag che vedi sotto
 , sostituendo "user" e "password"
    con l' user e password scelti per registrarti.</p>
<p id="p_content" class="p_content"><a href="https://breakingweb.site/webtalk/admin/">Pagina Di Amministrazione</a></p>
</div></div>

            <div class="col-7 text-left" id="id_video">
            <iframe width="320" height="240" src="https://www.youtube.com/embed/GN0FIFpRiWQ"
            title="Host-WebTalk" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media;
            gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
    </div>
</div>
</header>
<div class="container">
<div class="row justify-content-center">
<div id="div_col_installazione" class="col-lg-12">
    <p id="p_content" class="p_content"> .
   <pre>
       &lt;link rel=stylesheet href="https://breakingweb.site/static/css/blog.css">
       &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js">
          &lt;/script>
       &lt;script src="https://breakingweb.site/static/js/blog.js"> &lt;/script>
         &lt;script id="s_blog">initBlogSGang(document.title,<span style="color:blue">"user","password"</span>)>&lt;/script>
        </pre>

</p>
</div>
</div>
</div>
        </header>
        <footer>
 <link rel=stylesheet href="/static/css/blog.css">
       <script src="/static/js/blog.js"></script>
         <script id="s_blog">initBlogSGang("mario45","sol-7373") </script>

        </footer>
        </body>
        </html>"""
        return HttpResponse(page)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
