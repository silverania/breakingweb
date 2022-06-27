
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect


def user_login(request):
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
                    valuenext = request.POST.get('next')
                    return redirect(valuenext)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'compilare_il_kernel.html')


@login_required
def dashboard(request):
    return render(request, ' user/dashboard.html', {'section': 'dashboard'})


class LogoutView():
    def logout(request):
        logout(request)
        redirect_to = self.request.GET.get("next", "/")
        print("redirect to"+redirect_to)
        return redirect_to


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # photo = form.cleaned_data.get('photo')
            myphoto = request.POST.get('photo', False)
            user.profile.photo = myphoto
            user.profile.first_name = form.cleaned_data.get('username')
            user.save()
            print("USERPROFILEPHOTO"+str(myphoto))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/user/login')
    else:
        form = SignUpForm()
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
