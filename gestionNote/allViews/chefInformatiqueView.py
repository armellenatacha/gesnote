from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def chefInformatiqueList(request):
    
    template_name = 'listChefInformatique/listChefInformatique.html'
    listChefInformatique = ChefInformatique.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        userChefInfo = User.objects.filter(email=request.POST.get('email'), is_active=True)
        if not userChefInfo:
            userChefInfo1 = User.objects.filter(telephone=request.POST.get('telephone'), is_active=True)
            if not userChefInfo1:
                # Ici on
                user = User()
                user.nom = request.POST.get('nom')
                user.set_password("ChefInfo1234.")
                user.prenom = request.POST.get('prenom')
                user.telephone = request.POST.get('telephone')
                user.email = request.POST.get('email')
                user.chefInformatique = True
                # user.is_staff = False
                user.save()

                chefInfo = ChefInformatique()
                chefInfo.chef_informatique = user
                chefInfo.save()

                msg = "Opération effectuer avec succèss"
                print(msg)
                return render(request, template_name, {'listChefInformatique': listChefInformatique, 'msg': msg})
            else:
                error = "Ce numéro de téléphone est déjà associé à un compte"
                print(error)
                return render(request, template_name, {'listChefInformatique': listChefInformatique, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
        else:
            error = "Cet email est déjà associé à un compte"
            print(error)
            return render(request, template_name, {'listChefInformatique': listChefInformatique, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
    else:
        return render(request, template_name, {'listChefInformatique': listChefInformatique})


@login_required(login_url="/login/")
def chefInformatiqueUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'listChefInformatique/listChefInformatique.html'
    listChefInformatique = ChefInformatique.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        chefInformatiqueUserQuery = User.objects.filter(pk=request.POST.get('idUser'))
        chefInformatiqueQuery = ChefInformatique.objects.filter(pk=request.POST.get('id'))

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        if chefInformatiqueQuery and chefInformatiqueUserQuery:
            chefInformatiqueUser = User.objects.get(pk=request.POST.get('idUser'))
            chefInformatique = ChefInformatique.objects.get(pk=request.POST.get('id'))

            if User.objects.filter(Q(telephone=telephone) & ~Q(pk=chefInformatiqueUser.id)):
                error = "Impossible de modifier le contact car le numero de téléphone: "+telephone+" est déjà lié à un compte. Veuillez choisir un autre numéro"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listChefInformatique': listChefInformatique})
            elif User.objects.filter(Q(email=email) & ~Q(pk=chefInformatiqueUser.id)):
                error = "Impossible de modifier l'email car "+email+" est déjà lié à un compte.Veuillez choisir un autre email"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listChefInformatique': listChefInformatique})
            else:
                User.objects.filter(pk=request.POST.get('idUser')).update(
                    nom = nom,
                    prenom = prenom,
                    telephone = telephone,
                    email = email
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listChefInformatique': listChefInformatique})
    else:
        return render(request, template_name, {'listChefInformatique': listChefInformatique})


@login_required(login_url="/login/")
def chefInformatiqueDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'listChefInformatique/listChefInformatique.html'
    listChefInformatique = ChefInformatique.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        chefInformatiqueQuery = ChefInformatique.objects.filter(pk=request.POST.get('id'))
        chefInformatiqueUserQuery = User.objects.filter(pk=request.POST.get('idUser'))

        if chefInformatiqueQuery and chefInformatiqueUserQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                chefInformatiqueQuery.update(is_active=True)
                chefInformatiqueUserQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listChefInformatique': listChefInformatique})
            elif request.POST.get('is_active') == 'False':
                chefInformatiqueQuery.update(is_active=False)
                chefInformatiqueUserQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listChefInformatique': listChefInformatique})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listChefInformatique': listChefInformatique})
    else:
        return render(request, template_name, {'listChefInformatique': listChefInformatique})

