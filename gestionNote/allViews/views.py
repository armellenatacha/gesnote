from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from gestionNote.models import *
from django.shortcuts import *
from django.contrib.auth import login, authenticate, logout
# import request

# Create your views here.

def auth_login(request):
    if (request.method == 'POST'):
        logins = request.POST.get('username')
        mdp = request.POST.get('password')
        try:
            if request.POST.get('remember'):
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

        except MultiValueDictKeyError:
            is_private = False
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        user = authenticate(email=logins, password=mdp)
        if user:
            login(request, user)
            return redirect('accueil')
        else:
            return render(request, 'layouts/login.html',{'error': "informations invalides", 'email': login, 'mdp': mdp})
        
    else:   
        return render(request, 'layouts/login.html')

@login_required(login_url="/login/")
def auth_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login/")
def show_home(request):
    return render(request, 'acceuil.html')


