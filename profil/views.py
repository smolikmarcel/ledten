from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import UserExtend
from .forms import UserRegisterForm, UserExtendRegisterForm, UserUpdateForm, UserExtendUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='profil:prihlaseni')
def profil(request, user):
    context = {
        'Euser': UserExtend.objects.get(username=user),
        'user': User.objects.get(username=user)
    }

    return render(request, 'profil/profil.html', context)

@login_required(login_url='profil:prihlaseni')
def objednavky(request, user):
    context = {
        'Euser': UserExtend.objects.get(username=user),
        'user': User.objects.get(username=user)
    }

    return render(request, 'profil/objednavky.html', context)

@login_required(login_url='profil:prihlaseni')
def recenze(request, user):
    context = {
        'Euser': UserExtend.objects.get(username=user),
        'user': User.objects.get(username=user)
    }

    return render(request, 'profil/recenze.html', context)

@login_required(login_url='profil:prihlaseni')
def nastaveni(request, user):
    user = User.objects.get(username=user)
    Euser = UserExtend.objects.get(username=user)

    if request.method == 'POST':

        u_Euser = UserExtendUpdateForm(request.POST,
                                       request.FILES,
                                       instance=Euser)

        u_user  = UserUpdateForm(request.POST,
                                 instance=user)

        if u_Euser.is_valid() and u_user.is_valid():
            u_Euser.username = u_user.get('username')

            u_Euser.save()
            u_user.save()

    else:
        u_Euser = UserExtendUpdateForm(instance=Euser)
        u_user  = UserUpdateForm(instance=user)



    context = {
        'Euser': UserExtend.objects.get(username=user),
        'user': User.objects.get(username=user),
        'u_Euser': UserExtend.objects.get(username=user),
        'u_user': User.objects.get(username=user)
    }

    return render(request, 'profil/nastaveni.html', context)

@login_required(login_url='profil:prihlaseni')
def odhlasit(request):
    if request.method=='POST':
        logout(request)
        return render(request, 'homepage.html')

def prihlaseni(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            #log in user
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else:
                return redirect('profil:profil', user=user)

        else:
            messages.error(request, 'Ups heslo nebo jmeno neodpovídá.')

    else:
        form = AuthenticationForm()

    context = {
        'form': AuthenticationForm()
    }

    return render(request, 'profil/prihlaseni.html', context)

def registrace(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        eForm = UserExtendRegisterForm(request.POST)

        if form.is_valid() and eForm.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)

            eForm.username = username
            obj = eForm.save(commit=False)
            obj.save()

            return redirect('homepage')

        else:
            messages.error(request, 'Ups něco se stalo. Zkontrolujete jestli jsou všechny podmínky splněny')


    context = {
        'form': UserRegisterForm(),
        'eForm': UserExtendRegisterForm(),
    }

    return render(request, 'profil/registrace.html', context)
