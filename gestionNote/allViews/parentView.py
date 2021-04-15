from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def parentList(request):
    
    template_name = 'listParent/listParent.html'
    listParent = Parent.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        userParent = User.objects.filter(email=request.POST.get('email'), is_active=True)
        if not userParent:
            userParent1 = User.objects.filter(telephone=request.POST.get('telephone'), is_active=True)
            if not userParent1:
                # Ici on
                user = User()
                user.nom = request.POST.get('nom')
                user.set_password("parent1234.")
                user.prenom = request.POST.get('prenom')
                user.telephone = request.POST.get('telephone')
                user.email = request.POST.get('email')
                user.parent = True
                # user.is_staff = False
                user.save()

                parent = Parent()
                parent.parentUser = user
                parent.save()

                msg = "Opération effectuer avec succèss"
                print(msg)
                return render(request, template_name, {'listParent': listParent, 'msg': msg})
            else:
                error = "Ce numéro de téléphone est déjà associé à un compte"
                print(error)
                return render(request, template_name, {'listParent': listParent, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
        else:
            error = "Cet email est déjà associé à un compte"
            print(error)
            return render(request, template_name, {'listParent': listParent, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
    else:
        return render(request, template_name, {'listParent': listParent})


@login_required(login_url="/login/")
def parentUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'listParent/listParent.html'
    listParent = Parent.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        parentUserQuery = User.objects.filter(pk=request.POST.get('idUser'))
        parentQuery = Parent.objects.filter(pk=request.POST.get('id'))

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        if parentQuery and parentUserQuery:
            parentUser = User.objects.get(pk=request.POST.get('idUser'))
            parent = Parent.objects.get(pk=request.POST.get('id'))

            if User.objects.filter(Q(telephone=telephone) & ~Q(pk=parentUser.id)):
                error = "Impossible de modifier le contact car le numero de téléphone: "+telephone+" est déjà lié à un compte. Veuillez choisir un autre numéro"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listParent': listParent})
            elif User.objects.filter(Q(email=email) & ~Q(pk=parentUser.id)):
                error = "Impossible de modifier l'email car "+email+" est déjà lié à un compte.Veuillez choisir un autre email"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listParent': listParent})
            else:
                User.objects.filter(pk=request.POST.get('idUser')).update(
                    nom = nom,
                    prenom = prenom,
                    telephone = telephone,
                    email = email
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listParent': listParent})
    else:
        return render(request, template_name, {'listParent': listParent})


@login_required(login_url="/login/")
def parentDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'listParent/listParent.html'
    listParent = Parent.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        parentQuery = Parent.objects.filter(pk=request.POST.get('id'))
        parentUserQuery = User.objects.filter(pk=request.POST.get('idUser'))

        if parentQuery and parentUserQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                parentQuery.update(is_active=True)
                parentUserQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listParent': listParent})
            elif request.POST.get('is_active') == 'False':
                parentQuery.update(is_active=False)
                parentUserQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listParent': listParent})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listParent': listParent})
    else:
        return render(request, template_name, {'listParent': listParent})

