from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def eleveList(request):

    template_name = 'listEleve/listEleve.html'
    listEleve = Eleve.objects.filter(is_active=True)
    listParent = Parent.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        eleveExistant = Eleve.objects.filter(matricule=request.POST.get('matricule'), is_active=True)
        if not eleveExistant:

            eleve = Eleve()
            eleve.nom = request.POST.get('nom')
            eleve.prenom = request.POST.get('prenom')
            eleve.matricule = request.POST.get('matricule')
            eleve.sexe = request.POST.get('sexe')
            eleve.date_naissance = request.POST.get('date_naissance')
            eleve.lieu_naissance = request.POST.get('lieu_naissance')
            if request.POST.get('parent'):
                eleve.parentEleve = Parent.objects.get(pk=request.POST.get('parent'))
            if request.POST.get('classe'):
                eleve.classe = Classe.objects.get(pk=request.POST.get('classe'))
            eleve.is_eleve = True
            eleve.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse, 'msg': msg})
        else:
            error = "Ce matricule est déjà associé à un élève"
            return render(request, template_name, {'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse, 'error': error, 'nom': request.POST.get('nom'), 'prenom': request.POST.get('prenom'), 'matricule': request.POST.get('matricule'), 'date_naissance': request.POST.get('date_naissance'), 'lieu_naissance': request.POST.get('lieu_naissance'), 'parentEleve': request.POST.get('parent'), 'classeEleve': request.POST.get('classe'), 'sexe': request.POST.get('sexe')})
    else:
        return render(request, template_name, {'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})


@login_required(login_url="/login/")
def eleveUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'listEleve/listEleve.html'
    listEleve = Eleve.objects.filter(is_active=True)
    listParent = Parent.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        eleveQuery = Eleve.objects.filter(pk=request.POST.get('id'))

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        matricule = request.POST.get('matricule')
        date_naissance = request.POST.get('date_naissance')
        lieu_naissance = request.POST.get('lieu_naissance')
        parent = request.POST.get('parent')
        classe = request.POST.get('classe')
        sexe = request.POST.get('sexe')

        if eleveQuery:
            eleve = Eleve.objects.get(pk=request.POST.get('id'))

            if Eleve.objects.filter(Q(matricule=matricule) & ~Q(pk=eleve.id)):
                error = "Impossible de modifier le matricule: "+matricule+" est déjà lié à un élève. Veuillez choisir un autre matricule"
                return render(request, template_name, {'error': error, 'nom': nom, 'prenom': prenom, 'matricule': matricule, 'date_naissance': date_naissance, 'lieu_naissance': lieu_naissance, 'parentEleve': parent, 'sexe': sexe, 'classeEleve': classe, 'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})
            else:
                if request.POST.get('classe'):
                    Eleve.objects.filter(pk=request.POST.get('id')).update(
                        nom = nom,
                        prenom = prenom,
                        matricule = matricule,
                        date_naissance = date_naissance,
                        lieu_naissance = lieu_naissance,
                        sexe = sexe,
                        parentEleve = Parent.objects.get(pk=int(parent)),
                        classe = Classe.objects.get(pk=int(classe))
                    )
                else:
                    Eleve.objects.filter(pk=request.POST.get('id')).update(
                        nom = nom,
                        prenom = prenom,
                        matricule = matricule,
                        date_naissance = date_naissance,
                        lieu_naissance = lieu_naissance,
                        sexe = sexe,
                        parentEleve = Parent.objects.get(pk=int(parent))
                    )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})
    else:
        return render(request, template_name, {'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})


@login_required(login_url="/login/")
def eleveDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'listEleve/listEleve.html'
    listEleve = Eleve.objects.filter(is_active=True)
    listParent = Parent.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        eleveQuery = Eleve.objects.filter(pk=request.POST.get('id'))

        if eleveQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                eleveQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})
            elif request.POST.get('is_active') == 'False':
                eleveQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})
    else:
        return render(request, template_name, {'listEleve': listEleve, 'listParent': listParent, 'listClasse': listClasse})


@login_required(login_url="/login/")
def listEleveBulSeq(request):
    tempale_name = 'resultat/bulletinSequentielle/listEleveBulSeq.html'
    listClasse = Classe.objects.filter(is_active=True)

    return render(request, tempale_name, {'listClasse': listClasse})


@login_required(login_url="/login/")
def listEleveBulTrim(request):
    tempale_name = 'resultat/bulletinTrimestrielle/listEleveBulTrim.html'
    listClasse = Classe.objects.filter(is_active=True)

    return render(request, tempale_name, {'listClasse': listClasse})