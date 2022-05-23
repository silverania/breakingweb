from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import path
import os
from django.contrib.auth import login, authenticate
from .forms import UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.template import Template, Context
from django.template.loader import get_template
#from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def login(request):
  return render(request, 'login_success.html')


@login_required
def home(request):
  return render(request, 'compilare_il_kernel.html')


@login_required
def dashboard(request):
    return render(request, ' user/dashboard.html', {'section': 'dashboard'})


"""
def user_login(request):
    print("Entry In USER_LOGIN")
    if request.method == 'POST':
        print("request="+str(request))
        form = LoginForm(request.POST)
        if form.is_valid():
            t = get_template('login_success.html')
            html = t.render()
            cd = form.cleaned_data
            user = authenticate(
                 request, username=cd['username'], password=cd['password'])
            print("USER"+str(user))
            if user is not None:
                if user.is_active:
                    login(request)
                    return HttpResponse(html)
                else:
                    return HttpResponse('Disabled account')
                ({'password_error': '<span class=\"tag tag-danger\">Password Errata!</span>'})

    else:
        if request.user.is_authenticated:
            return HttpResponse("Utente gia autenticato !!")
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})
"""


class LogoutView():
    def logout(request):
        logout(request)
        redirect_to = self.request.GET.get("next", "/")
        print("redirect to"+redirect_to)
        return redirect_to


def user_register(request):

    #print(data["user"])
    #body = request.body.decode('utf-8')
    #body = json.loads(str(body))
    #data2 = body["password"]

    if request.method == 'POST':
        data = (dict(request.POST.lists()))
        print(str(data["Nome"]))
        print("FORM VALIDO")
        # Create a new user object but avoid saving it yet
        # new_user = user_form.save(commit=False)
        # Set the chosen password
        new_user = User.objects.create_user(
          str(data['Nome']), str(data['Email']), str(data['password']))
        # Save the User object
        new_user.set_password(str(data['password']))
        new_user.save()
        profile = Profile.objects.get(user=new_user)
        if "/user/register" in reaquest.path:
            profile.profile_reg_to_application = "blog"
        print("PROFILE USERNAME "+profile.first_name)
        profile.first_name = new_user.username
        profile.save()
        return render(request, 'user/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'user_form': user_form})


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
