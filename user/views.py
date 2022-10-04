from django.conf import settings
from .forms import UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
import json
from django.core import serializers
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
list_current_user = None
scrollTo = ''
Profile = Profile.objects.all()
Group = Group.objects.all()


def getUser(user):
    list_current_user = []
    global Profile
    firstName = str(user)
    current_user = Profile.filter(first_name=firstName)
    list_current_user = list(current_user)
    list_current_user = serializers.serialize(
        "json", list_current_user)
    return list_current_user


@method_decorator(csrf_exempt, name='dispatch')
class checkUser(View):
    def post(self, request):
        userLoggedIN = request.user.is_authenticated
        myuser = object()
        userThatLoginIn = object()
        list_json_user_data = json.loads(request.body)
        print("json : "+str(list_json_user_data))
        for key, value in list_json_user_data.items():
            if 'user' in key:
                myuser = value
            if 'password' in key:
                password = value
        if not bool(userLoggedIN):
            print("if userloggedin mi da : " + str(userLoggedIN))
        if not isinstance(myuser, User):
            try:
                myuser = authenticate(username=myuser, password=password)
                print("Verifica ... myuser non è di tipo User , ho proceduto"
                      + "ad authenticazione !! verifico se sta nel gruppo Blog.."+str(myuser))
                if myuser.groups.filter(name__in=['BlogAdmin']).exists():
                    print("myuser sta già nel gruppo blog_admin.....")
                else:
                    print("user myuser NON sta nel gruppo blog_admin.....provvedo"
                          + "ad aggiungerlo ....")
                    group = Group.get(name='BlogAdmin')
                    myuser.groups.add(group)
                    print('myuser aggiunto al gruppo blogadmin ')
            except Exception:
                print("Errore nel autenticazione dell user , e/o nella sua assegnazione"
                      + "al gruppo BlogAdmin")
                myuser = "None"
                list_current_user = myuser
        else:
            print(
                "L user era autentticato non c' è stato bisogno di ripetere l autenticaxzione"
                'L user è autenticato . la funzione request.user mi da : '+str(request.user))
        if isinstance(myuser, User):
            list_current_user = getUser(myuser)
        if isinstance(request.user, User):
            userThatLoginIn = request.user.username
            userThatLoginIn = getUser(userThatLoginIn)
        else:
            userThatLoginIn = "None"
        data = json.dumps(
            {
                "userLogged": list_current_user,
                "userLoggedIN": userThatLoginIn,
                "authenticated": request.user.is_authenticated,
                "user": str(request.user),
            })
        print(str(JsonResponse(data, safe=False)))
        response = JsonResponse(
            data, safe=False
        )
        return response

    def get(self, request):
        return HttpResponse("GET")

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
    global te, scrollTo
    userLoggedIN = User
    valuenext = ""
    if 'next' in request.GET:
        valuenext = request.GET.get('next')+scrollTo
        print("entry in view user_login....valuenext="+valuenext)
    password = ''
    print("login="+str(request.user.is_authenticated))
    try:
        if request.user.is_authenticated:
            return render(request, "seigiaautenticato.html", {'valuenext':
                                                              valuenext})
    except Exception:
        print("userLoggedihn non riesco a sapere lo stato Auth/nonauth")
    if request.method == 'POST':
        if 'next' in request.POST:
            valuenext = request.POST.get('next')+scrollTo
            print("view: user_login , POST method......valuenext="+valuenext)
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            myuser = authenticate(request,
                                  username=cd['username'],
                                  password=cd['password'])
            if myuser is not None:
                if myuser.is_active:
                    login(request, myuser)
                    # userLoggedIN = myuser
                    return HttpResponseRedirect(valuenext)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        if request.method == 'GET':
            if 'blog' in request.get_full_path():
                scrollTo = "#footer"
            if 'next' in request.GET:
                valuenext = request.GET.get('next')+scrollTo
                subject = 'welcome to GFG world'
                message = 'Hi mario, thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ["info.strabbit@gmail.com", ]
                # send_mail(subject, message, email_from, recipient_list)
            myuser = None
            print("view: user_login , GET method......valuenext="+valuenext)
    return render(request, 'registration/login.html', {'form': form,
                                                       'next': valuenext, 'user': myuser, 'password': password})


@login_required
def home(request):
    return render(request, 'compilare_il_kernel.html')


@login_required
def dashboard(request):
    return render(request, ' user/dashboard.html', {'section': 'dashboard'})


class Logout(View):
    def get(self, request):
        global userLoggedIN
        logout(request)
        userLoggedIN = None
        if 'next' in request.GET:
            print("next in request !")
            next = request.GET.get('next')
            template = "registration/logged_out.html"
            return redirect(next)
            #return render(request, "seiuscito.html", {'valuenext': next})
        return render(request, "seiuscito.html", {'valuenext': next})


def user_register(request):
    valuenext = ""
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.profile.photo = form.cleaned_data.get('photo')
            user.profile.first_name = username
            if 'bloguser' in request.path:
                valuenext = request.GET.get('next')
                return redirect('/user/login/blog?next='+valuenext)
            elif 'blog' in request.path:
                group = Group.get(name='BlogAdmin')
                user.groups.add(group)
                print('myuser'+str(user)
                      + "aggiunto al gruppo blogadmin ")
                user.is_staff = True
                user.save()
                # mostra messaggio e esci
                return HttpResponse("sei autorizzato ad usare hostMessage !")
            else:
                user = authenticate(username=username, password=raw_password)
            print("USERPROFILEPHOTO"+str(request.FILES))
            # vai alla pagina per utenti blog : "la home del sito su cui è installato già il blog"
            if 'next' in request.GET:
                valuenext = request.GET.get('next')
                return redirect('/user/login?next='+valuenext)
            else:
                return redirect('/user/login')
    else:
        """
        if 'blog' in request.path and 'next' in request.GET:
            scrollTo = '#footer'
            valuenext = request.GET.get('next')+scrollTo
        elif 'blog' in request.path:
            scrollTo = '#footer'
        elif 'next' in request.GET:
            valuenext = request.GET.get('next')
            """
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            if 'next' in request.GET:
                valuenext = request.GET.get('next')
                breakpoint()
                return render(request, "registration/pass_changed_done.html", {'valuenext': valuenext})
        else:
            return HttpResponse("errore nei dati inseriti !")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


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
