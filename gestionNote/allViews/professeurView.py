from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def listProfesseur(request):

    template_name = 'listProfesseur/listProfesseur.html'
    listProfesseur = Professeur.objects.filter(is_active=True)
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        userProfesseur = User.objects.filter(email=request.POST.get('email'), is_active=True)
        if not userProfesseur:
            userProfesseur1 = User.objects.filter(telephone=request.POST.get('telephone'), is_active=True)
            if not userProfesseur1:

                lesMatieres = request.POST.getlist('matiere')
                # Ici on
                user = User()
                user.nom = request.POST.get('nom')
                user.set_password("Professeur1234.")
                user.prenom = request.POST.get('prenom')
                user.telephone = request.POST.get('telephone')
                user.email = request.POST.get('email')
                user.professeur = True
                # user.is_staff = False
                user.save()

                professeur = Professeur()
                professeur.professeurUser = user
                professeur.save() 
                if lesMatieres:
                    for matiere in lesMatieres:
                        # print(Matiere.objects.get(pk=lesMatieres))
                        professeur.professeurMatiere.add(Matiere.objects.get(pk=matiere))  

                # print(professeur)

                msg = "Opération effectuer avec succèss"
                print(msg)
                return render(request, template_name, {'listProfesseur': listProfesseur, 'listMatiere': listMatiere, 'msg': msg})
            else:
                error = "Ce numéro de téléphone est déjà associé à un compte"
                print(error)
                return render(request, template_name, {'listProfesseur': listProfesseur, 'listMatiere': listMatiere, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
        else:
            error = "Cet email est déjà associé à un compte"
            print(error)
            return render(request, template_name, {'listProfesseur': listProfesseur, 'listMatiere': listMatiere, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'telephone': request.POST.get('telephone'), 'email': request.POST.get('email')})
    else:
        return render(request, template_name, {'listProfesseur': listProfesseur, 'listMatiere': listMatiere})


@login_required(login_url="/login/")
def professeurUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'listProfesseur/listProfesseur.html'
    listProfesseur = Professeur.objects.filter(is_active=True)
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        professeurUserQuery = User.objects.filter(pk=request.POST.get('idUser'))
        professeurQuery = Professeur.objects.filter(pk=request.POST.get('id'))

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        lesMatieres = request.POST.getlist('matiere')

        if professeurQuery and professeurUserQuery:
            professeurUser = User.objects.get(pk=request.POST.get('idUser'))
            professeur = Professeur.objects.get(pk=request.POST.get('id'))

            if User.objects.filter(Q(telephone=telephone) & ~Q(pk=professeurUser.id)):
                error = "Impossible de modifier le contact car le numero de téléphone: "+telephone+" est déjà lié à un compte. Veuillez choisir un autre numéro"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
            elif User.objects.filter(Q(email=email) & ~Q(pk=professeurUser.id)):
                error = "Impossible de modifier l'email car "+email+" est déjà lié à un compte.Veuillez choisir un autre email"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'telephone': telephone, 'email': email, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
            else:
                User.objects.filter(pk=request.POST.get('idUser')).update(
                    nom = nom,
                    prenom = prenom,
                    telephone = telephone,
                    email = email
                )
                if lesMatieres:
                    professeur.professeurMatiere.clear()
                    for matiere in lesMatieres:
                        # print(Matiere.objects.get(pk=lesMatieres))
                        professeur.professeurMatiere.add(Matiere.objects.get(pk=matiere)) 

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
    else:
        return render(request, template_name, {'listProfesseur': listProfesseur})


@login_required(login_url="/login/")
def professeurDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'listProfesseur/listProfesseur.html'
    listProfesseur = Professeur.objects.filter(is_active=True)
    listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        professeurQuery = Professeur.objects.filter(pk=request.POST.get('id'))
        professeurUserQuery = User.objects.filter(pk=request.POST.get('idUser'))

        if professeurQuery and professeurUserQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                professeurQuery.update(is_active=True)
                professeurUserQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
            elif request.POST.get('is_active') == 'False':
                professeurQuery.update(is_active=False)
                professeurUserQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listProfesseur': listProfesseur, 'listMatiere': listMatiere})
    else:
        return render(request, template_name, {'listProfesseur': listProfesseur, 'listMatiere': listMatiere})

