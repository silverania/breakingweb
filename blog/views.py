from django.shortcuts import render
from user.models import Profile
from blog.models import Comment, Resp, Site
from django.http import HttpResponse, JsonResponse
from django.utils import formats
from datetime import datetime
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from urllib.parse import urlsplit
import blog
photo = ""
message = ""
Profile = Profile.objects.all()
Comment = Comment.objects.all()
Resp = Resp.objects.all()
Site = Site.objects.all()
formatted_datetime = formats.date_format(
    datetime.now(), "SHORT_DATETIME_FORMAT")


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Resp.__class__) or isinstance(obj, Site.__class__):
            return str(obj)
        return super().default(obj)


def getLoginName(request):
    if request.user.is_authenticated:
        myuser = Profile.filter(user_id=request.user.id)
    else:
        myuser = Profile.filter(first_name="anonimo")
        #    myuser.photo = settings.MEDIA_URL+"images/user-secret-solid.gif"
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
    global formatted_datetime, Comment, Profile
    data = ""
    t = []
    datac = []
    comments = []
    comments_in_database = Comment.all()
    profiles = list(Profile.all())
    profiles_list = serializer(profiles)
    t2 = []
    if "tagTitle" in request.GET and request.GET["tagTitle"]:
        tagTitle = str(request.GET.get("tagTitle"))
        if comments_in_database.exists():
            all_comments_for_page = Comment.filter(
                site__title=tagTitle).order_by('-publish')
            datac = list(all_comments_for_page)
            data_comm = serializer(datac)
            if datac:
                for comment in all_comments_for_page:
                    try:
                        if tagTitle in str(comment.site.title):
                            comments.append(comment)
                            t_order = comment.risposte.all().order_by('-publish')
                            t = list(t_order)
                    except Exception:
                        continue
                    try:
                        if t2 is not None:
                            t2 = t2 + t
                    except UnboundLocalError:
                        t2 = t
                    try:
                        t2 = list(t2)
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
            data = json.dumps(
                {
                    "resps": [{"": ""}],
                    "data_comm": [{"": ""}],
                    "profiles": profiles_list,
                    }
                )
    return JsonResponse(data, safe=False)


def newPost(request):
    global Profile, Comment, Resp
    postType = ""
    post = []
    getRespOrPostToAssignResp = []
    if "body" in request.GET and request.GET["body"]:
        body = request.GET.get("body")
    if "username" in request.GET and request.GET["username"]:
        author = request.GET.get("username")
        myuser = Profile.get(first_name=author)
        myuser.firstname = getLoginName(request)
    if "tagTitle" in request.GET:
        tagTitle = request.GET.get('tagTitle')
        split_url = urlsplit(tagTitle)
        site = Site.get(
            title=split_url.scheme+"://"+split_url.netloc+split_url.path)
    if "type" in request.GET and request.GET["type"]:
        postType = request.GET.get("type")
        if "newpost" in postType:
            post = blog.models.Comment()
            post.postType = "post"
        else:
            post = blog.models.Resp()
            if "respToUser" in request.GET and request.GET["respToUser"]:
                respToProfile = request.GET.get("respToUser")
                respToProfile = Profile.get(first_name=respToProfile)
                post.respToUser = respToProfile
            if "respTo" in request.GET and request.GET["respTo"]:
                post.idRespTo = request.GET.get("respTo")
                if "commento" in request.GET and request.GET["commento"]:
                    commento = request.GET.get("commento")
                    comment = Comment.get(pk=commento)
                    post.commento = comment
                if 'respToType' in request.GET and request.GET["respToType"]:
                    respToType = request.GET.get('respToType')
                    if 'respToResp' in respToType:
                        post.postType = "respToResp"
                        getRespOrPostToAssignResp = Resp.get(
                            pk=post.idRespTo)
                    elif 'respToPost' in respToType:
                        getRespOrPostToAssignResp = Comment.get(
                            pk=commento)
                        post.commento = getRespOrPostToAssignResp
    post.site = site
    post.site.title = tagTitle
    post.slug = site.title.replace("/", "")
    post.slug = site.title.replace(":", "")
    post.author = myuser
    # post.site.user = myuser
    post.site.titleTagContent = tagTitle
    post.publish = datetime.now()
    post.created = post.publish
    post.body = body
    post.save()
    typeIs = str(type(getRespOrPostToAssignResp))
    if "Resp" in typeIs:
        getRespOrPostToAssignResp.resps.add(post)
    return HttpResponse("post inserito")


def retReverse(name):
    return reverse("blog:" + name)
