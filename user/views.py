
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
import json
from django.core import serializers
from django.contrib.auth.models import User, AnonymousUser
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
valuenext = ""


@method_decorator(csrf_exempt, name='dispatch')
class checkUser(View):

    def post(self, request):
        global valuenext
        list_json_user_data = json.loads(request.body)
        print("json : "+str(list_json_user_data))
        for key, value in list_json_user_data.items():
            if 'user' in key:
                user = value
            if 'password' in key:
                password = value
        user = authenticate(username=user, password=password)
        #userRequestFor = list_json_user_data['user']
        user_authenticated = user
        print("lmmmmmmm"+str(user.username))
        if not isinstance(user_authenticated, AnonymousUser):
            firstName = user_authenticated.username
            print("lmmmmmmm"+str(firstName))
            current_user = Profile.objects.filter(first_name=firstName)
            list_current_user = list(current_user)
            list_current_user = serializers.serialize(
                "json", list_current_user)
        else:
            #breakpoint()
            current_user = Profile.objects.filter(first_name="anonimo")
            #breakpoint()
            list_current_user = list(current_user)
            list_current_user = serializers.serialize(
                "json", list_current_user)
            #breakpoint()
        c = get_token(request)
        print("CCCCCCC="+str(c))
        data = json.dumps(
            {
                "request": c, "userLogged": list_current_user,
            })
        print(str(JsonResponse(data, safe=False)))
        response = JsonResponse(
            data, safe=False
        )
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request)
        elif request.method == 'POST':
            cv = request.body
            print("from dispatch method :"+str(cv))
            return self.post(request, *args, **kwargs)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def getUrlRequest(request):
    urls = request.build_absolute_uri()
    return urls


def user_login(request):
    global te, valuenext
    c = get_token(request)
    if request.user.is_authenticated:
        return HttpResponse("Sei già autenticat !")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            myuser = authenticate(request,
                                  username=cd['username'],
                                  password=cd['password'])
            if myuser is not None:
                if myuser.is_active:
                    login(request, myuser)
                    return HttpResponseRedirect(valuenext)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        if request.method == 'GET':
            if 'next' in request.GET:
                valuenext = request.GET.get('next')
    return render(request, 'registration/login.html', {'form': form, 'next': valuenext})


@login_required
def home(request):
    return render(request, 'compilare_il_kernel.html')


@login_required
def dashboard(request):
    return render(request, ' user/dashboard.html', {'section': 'dashboard'})


class Logout(View):
    def get(self, request):
        logout(request)
        #redirect_to = self.request.GET.get("next", "/")
        template = "registration/logged_out.html"
        return render(request, template)


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.photo = form.cleaned_data.get('photo')
            # myphoto = request.FILES('photo')
            # user.profile.photo = myphoto
            user.profile.first_name = form.cleaned_data.get('username')
            user.save()
            print("USERPROFILEPHOTO"+str(request.FILES))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if 'blog' in request.path:
                return redirect('/user/login/blog')
            return redirect('/user/login')
    else:
        form = SignUpForm()
        #print("USERPROFILEPHOTO"+str(myphoto))
    return render(request, 'user/register.html', {'form': form})


@ login_required
def edit(request):
    print("request="+str(request))
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request, 'edit.html', {'user_form': user_form, 'profile_form': profile_form})
