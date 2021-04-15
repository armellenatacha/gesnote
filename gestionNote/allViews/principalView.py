from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def principalList(request):
    
    template_name = 'listPrincipal/listPrincipal.html'
    listPrincipal = Principal.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        userPrincipal = User.objects.filter(email=request.POST.get('email'), is_active=True)
        if not userPrincipal:
            userPrincipal1 = User.objects.filter(telephone=request.POST.get('telephone'), is_active=True)
            if not userPrincipal1:
                # Ici on
                user = User()
                user.nom = request.POST.get('nom')
                user.set_password("principal1234.")
                user.prenom = request.POST.get('prenom')
                user.telephone = request.POST.get('telephone')
                user.email = request.POST.get('email')
                user.principal = True
                # user.is_staff = False
                user.save()

                principal = Principal()
                principal.principalUser = user
                principal.save()

                msg = "Opération effectuer avec succèss"
                print(msg)
                return render(request, template_name, {'listPrincipal': listPrincipal, 'msg': msg})
            else:
                error = "Ce numéro de téléphone est déjà associé à un compte"
                print(error)
                return render(request, template_name, {'listPrincipal': listPrincipal, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
        else:
            error = "Cet email est déjà associé à un compte"
            print(error)
            return render(request, template_name, {'listPrincipal': listPrincipal, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
    else:
        return render(request, template_name, {'listPrincipal': listPrincipal})


@login_required(login_url="/login/")
def principalUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'listPrincipal/listPrincipal.html'
    listPrincipal = Principal.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        principalUserQuery = User.objects.filter(pk=request.POST.get('idUser'))
        principalQuery = Principal.objects.filter(pk=request.POST.get('id'))

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        if principalQuery and principalUserQuery:
            principalUser = User.objects.get(pk=request.POST.get('idUser'))
            principal = Principal.objects.get(pk=request.POST.get('id'))

            if User.objects.filter(Q(telephone=telephone) & ~Q(pk=principalUser.id)):
                error = "Impossible de modifier le contact car le numero de téléphone: "+telephone+" est déjà lié à un compte. Veuillez choisir un autre numéro"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listPrincipal': listPrincipal})
            elif User.objects.filter(Q(email=email) & ~Q(pk=principalUser.id)):
                error = "Impossible de modifier l'email car "+email+" est déjà lié à un compte.Veuillez choisir un autre email"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listPrincipal': listPrincipal})
            else:
                User.objects.filter(pk=request.POST.get('idUser')).update(
                    nom = nom,
                    prenom = prenom,
                    telephone = telephone,
                    email = email
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listPrincipal': listPrincipal})
    else:
        return render(request, template_name, {'listPrincipal': listPrincipal})


@login_required(login_url="/login/")
def principalDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'listPrincipal/listPrincipal.html'
    listPrincipal = Principal.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        principalQuery = Principal.objects.filter(pk=request.POST.get('id'))
        principalUserQuery = User.objects.filter(pk=request.POST.get('idUser'))

        if principalQuery and principalUserQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                principalQuery.update(is_active=True)
                principalUserQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listPrincipal': listPrincipal})
            elif request.POST.get('is_active') == 'False':
                principalQuery.update(is_active=False)
                principalUserQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listPrincipal': listPrincipal})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listPrincipal': listPrincipal})
    else:
        return render(request, template_name, {'listPrincipal': listPrincipal})

