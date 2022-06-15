from django.shortcuts import render, redirect
from user.models import Profile
from blog.models import Comment, Resp, Site
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.utils import formats
from datetime import datetime
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse

photo = ""
message = ""
tu = Site()
site = ""
formatted_datetime = formats.date_format(
    datetime.now(), "SHORT_DATETIME_FORMAT")


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Resp) or isinstance(obj, Site):
            return str(obj)
        return super().default(obj)


def getLoginName(request):
    try:
        if request.user.is_authenticated:
            print("id" + str(request.user.id))
            myuser = Profile.objects.filter(user_id=request.user.id)
        else:
            #user = request.GET.get("loginis")
            myuser = Profile.objects.filter(first_name="anonimo")
            myuser.photo = settings.MEDIA_URL+"images/user-secret-solid.gif"
            print("SER NON AUTENT " + str(myuser.photo))
    except UnboundLocalError:
        print("error in get users info ! contact the admin . myuser = " + str(myuser))
    return myuser


def serializer(data):
    datas = serializers.serialize(
        "json",
        data,
        cls=LazyEncoder,
        use_natural_primary_keys=True,
        use_natural_foreign_keys=True,
    )
    return datas


def getPost(request):

    print("entry in view getpost")
    global tu, formatted_datetime, tagTitle, site
    profile_list = []
    datac = []
    comments = []
    # resps = Resp.objects.all()
    # risposte = []
    # risposte_serialized = []
    comments_in_database = Comment.objects.all().order_by('publish')
    userLogged = getLoginName(request)
    userLogged = list(userLogged)
    userLogged = serializer(userLogged)
    profiles = list(Profile.objects.all())
    profiles_list = serializer(profiles)
    # breakpoint()
    if comments_in_database.exists():
        print("COMMENTS in DATABASES"+str(comments_in_database))
        # userLogged = getLoginName(request)
        print("USERLOGGED=" + str(userLogged))
        resps = Resp.objects.all()
        risposte = []
        risposte_serialized = []
        if "tagTitle" in request.GET and request.GET["tagTitle"]:
            tagTitle = str(request.GET.get("tagTitle"))
            tu.title = tagTitle
            print("tagtitle=" + str(tagTitle))
            #tagTitleInPage = Site.objects.get(title=tagTitle)
            aggiornato = formatted_datetime
            all_comments_for_page = Comment.objects.filter(
                site__title=tagTitle).order_by('-publish')
            datac = list(all_comments_for_page)
            # userLogged = list(userLogged)
            # userLogged = serializer(userLogged)
            data_comm = serializer(datac)
            comment_model_serialized = serializer(all_comments_for_page)
            print("data comment Json format=" + str(datac))
            print("comment_model_serialized="
                  + str(comment_model_serialized)+str("userLogged"+str(userLogged)))
            for comment in comments_in_database:
                print("tagtitle="+str(tagTitle)+"___"
                      + "comment.site="+str(comment.site))
                if tagTitle in str(comment.site):
                    comments.append(comment)
                    print("COMMENTS=" + str(comments))
                    #t_order = comment.risposte.all().order_by('publish')
                    t_order = comment.risposte.all().order_by('-publish')
                    t = list(t_order)
                    print("Resp=" + str(t))
                    try:
                        t2 = t2 + t
                    except UnboundLocalError:
                        t2 = t
                    try:
                        print("SERIALIZED :PROFILKE_LIST="+str(profile_list))
                        risposte_serialized = serializer(t2)
                        # profiles = list(Profile.objects.all())
                        # profiles_list = serializer(profiles)
                        print("PROFIKLELIST"+str(profiles_list))
                    except UnboundLocalError:
                        print("Nessun commento per la pagina !")
            data = json.dumps(
                {
                    "userLogged": userLogged,
                    "data_comm": data_comm,
                    "resps": risposte_serialized,
                    "profiles": profiles_list,
                    }
                )
    else:
        print("si e verificato else in getpost userlogged=  & profiles_list="
              + userLogged+"_"+profiles_list)
        data = json.dumps(
                {
                    "userLogged": userLogged,
                    "profiles": profiles_list,
                    }
                )
    try:
        return JsonResponse(data, safe=False)
    except UnboundLocalError:
        print("cahe sfcaccim")


def newPost(request):
    postType = ""
    print("entrypoint to newPost ....request="+str(request))
    # thistutorial=Tutorial()
    if "type" in request.GET and request.GET["type"]:
        postType = request.GET.get("type")
    if "newpost" in postType:
        post = Comment()
    else:
        post = Resp()
    myuser = Profile()
    myuser.firstname = getLoginName(request)
    # post.site = tu
    if "newpost" in postType:
        post.site = tu
        if "title" in request.GET and request.GET["title"]:
            title = request.GET.get("title")
            # post.title = title
            post.site.title = title
            post.slug = post.title.replace(" ", "_")
    post.publish = datetime.now()
    post.created = post.publish
    if "username" in request.GET and request.GET["username"]:
        author = request.GET.get("username")
        myuser = Profile.objects.get(first_name=author)
        print("user MYUSER=" + str(myuser))
        post.author = myuser

    if "body" in request.GET and request.GET["body"]:
        body = request.GET.get("body")
        post.body = body
    if "commento" in request.GET and request.GET["commento"]:
        commento = request.GET.get("commento")
        comment = Comment.objects.get(pk=commento)
        post.commento = comment
    tu.save()
    post.save()
    return HttpResponse("OK !")
    """
        if "resp" in type:
            r=Resp()
            r.body=message
            r.author=myuser
            r.authorname=myuser.username
            r.commento=post
            r.save()
            print(str("è una risposta:"+str(post.risposte)))
        else:
            tu.post=post
            post.body=message
            post.author=myuser
            post.authorname=myuser.username
            print("creato,autore:"+str(post.created)+str(post.author))
            aggiornato=formatted_datetime
        if 'tutorial' in request.GET and request.GET['tutorial'] :
                tu.post=post
                print("tu.post="+str(tu.post)+"risposta:"+str(tu.post.risposte.all()))

        """


def showPost(tutorial):
    print("entry in view showPost")
    thistutorial = tutorial.slug
    print("thistutorial=" + tutorial.slug)


def retReverse(name):
    return reverse("blog:" + name)
