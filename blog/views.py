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
data = {}
formatted_datetime = formats.date_format(
    datetime.now(), "SHORT_DATETIME_FORMAT")


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Resp) or isinstance(obj, Site):
            return str(obj)
        return super().default(obj)


"""
class authAdmin(View):
    def post(self,request):
    """


def getLoginName(request):
    try:
        if request.user.is_authenticated:
            print("id" + str(request.user.id))
            myuser = Profile.objects.filter(user_id=request.user.id)
        else:
            myuser = Profile.objects.filter(first_name="anonimo")
            #    myuser.photo = settings.MEDIA_URL+"images/user-secret-solid.gif"
            print("USER NON AUTENT ")
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
    global tu, formatted_datetime, tagTitle, site, data
    profile_list = []
    datac = []
    comments = []
    comments_in_database = Comment.objects.all()
    profiles = list(Profile.objects.all())
    profiles_list = serializer(profiles)
    t2 = []
    if "tagTitle" in request.GET and request.GET["tagTitle"]:
        tagTitle = str(request.GET.get("tagTitle"))
        tu, create = Site.objects.get_or_create(title=tagTitle)
        print("tagtitle=" + str(tagTitle))
        # tagTitleInPage = Site.objects.get(title=tagTitle)
        # aggiornato = formatted_datetime
        if comments_in_database.exists():
            risposte_serialized = []
            all_comments_for_page = Comment.objects.filter(
                site__title=tagTitle).order_by('-publish')
            datac = list(all_comments_for_page)
            data_comm = serializer(datac)
            for comment in comments_in_database:
                if tagTitle in str(comment.site):
                    comments.append(comment)
                    t_order = comment.risposte.all().order_by('-publish')
                    t = list(t_order)
                    try:
                        if t2 is not None:
                            t2 = t2 + t
                    except UnboundLocalError:
                        t2 = t
                    try:
                        risposte_serialized = serializer(t2)
                    except UnboundLocalError:
                        print("Nessun commento per la pagina !")
            data = json.dumps(
                {
                    "data_comm": data_comm,
                    "resps": risposte_serialized,
                    "profiles": profiles_list,
                    }
                )
        else:
            print("Errore ,Non ci sono commenti nel database !")
            data = json.dumps(
                {
                    "resps": [{"": ""}],
                    "data_comm": [{"": ""}],
                    "profiles": profiles_list,
                }
            )
        try:
            return JsonResponse(data, safe=False)
        except UnboundLocalError:
            print("cahe sfcaccim")
    return render(request, {'data': data, })


def newPost(request):
    global tu
    postType = ""
    print("entrypoint to newPost ....request="+str(request))
    if "type" in request.GET and request.GET["type"]:
        postType = request.GET.get("type")
        if "newpost" in postType:
            post = Comment.objects.create()
            post.postType = "post"
            post.site = tu
            post.slug = tu.title.replace(" ", "_")
            post.publish = datetime.now()
            post.created = post.publish
        else:
            post = Resp()
            if "respTo" in request.GET and request.GET["respTo"]:
                post.idRespTo = request.GET.get("respTo")
    myuser = Profile()
    myuser.firstname = getLoginName(request)
    if "username" in request.GET and request.GET["username"]:
        author = request.GET.get("username")
        myuser = Profile.objects.get(first_name=author)
        post.author = myuser
    if "respToUser" in request.GET and request.GET["respToUser"]:
        respToProfile = request.GET.get("respToUser")
        respToProfile = Profile.objects.get(first_name=respToProfile)
        post.respToUser = respToProfile
    if "body" in request.GET and request.GET["body"]:
        body = request.GET.get("body")
        post.body = body
    if "commento" in request.GET and request.GET["commento"]:
        commento = request.GET.get("commento")
        comment = Comment.objects.get(pk=commento)
        post.commento = comment
    if 'respToType' in request.GET and request.GET["respToType"]:
        respToType = request.GET.get('respToType')
        if 'respToResp' in respToType:
            post.postType = "respToResp"
            getRespOrPostToAssignResp = Resp.objects.get(pk=post.idRespTo)
            post.save()
            getRespOrPostToAssignResp.resps.add(post)
        elif 'respToPost' in respToType:
            getRespOrPostToAssignResp = Comment.objects.get(pk=commento)
            post.commento = getRespOrPostToAssignResp
    post.save()
    # post = serializers.serialize('json', [post], ensure_ascii=False)
    # json_post = json.dumps({'post': post})
    return HttpResponse("post inserito")


def showPost(tutorial):
    print("entry in view showPost")
    thistutorial = tutorial.slug
    print("thistutorial=" + tutorial.slug)


def retReverse(name):
    return reverse("blog:" + name)
