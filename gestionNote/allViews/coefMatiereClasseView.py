from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def listCoefMatiereClasse(request):
    
    template_name = 'Paramètre/listMatière/affecterCoefMatiereClasse.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    listCoefMatiereClasse = Classe_matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        classe_matiere = Classe_matiere.objects.filter(classe_m=request.POST.get('classe'), matiere_c=request.POST.get('matiere'), is_active=True)
        if not classe_matiere:
            # Ici on
            classe_matiere = Classe_matiere()
            classe_matiere.classe_m = Classe.objects.get(pk=request.POST.get('classe'))
            classe_matiere.matiere_c = Matiere.objects.get(pk=request.POST.get('matiere'))
            classe_matiere.coefficient_Matiere = request.POST.get('coefficient_Matiere')
            # classe_matiere.is_staff = False
            classe_matiere.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse, 'msg': msg})
        else:
            error = "Cette matière a déjà de coefficient pour cette classe"
            return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse, 'error': error, 'matiere': request.POST.get('matiere'), 'classe': request.POST.get('classe'), 'classes': request.POST.getlist('classe'), 'coefficient_Matiere': request.POST.get('coefficient_Matiere')})
    
    else:
        return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})


@login_required(login_url="/login/")
def updateCoefMatiereClasse(request):
    """
    Cette fonction permet de modifier les informations du coefficient
    """
    template_name = 'Paramètre/listMatière/affecterCoefMatiereClasse.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    listCoefMatiereClasse = Classe_matiere.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        classe_matiereQuery = Classe_matiere.objects.filter(pk=request.POST.get('id'))

        classe = request.POST.get('classe')
        matiere = request.POST.get('matiere')
        coefficient_Matiere = request.POST.get('coefficient_Matiere')

        if classe_matiereQuery:
            classe_matiere = Classe_matiere.objects.get(pk=request.POST.get('id'))

            if Classe_matiere.objects.filter(Q(classe_m=classe) & Q(matiere_c=matiere) & ~Q(pk=classe_matiere.id)):
                error = "Impossible de modifier le coefficient car cette matière possède déjà un coefficient pour cette classe"
                return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse, 'error': error, 'matiere': request.POST.get('matiere'), 'classe': request.POST.get('classe'), 'classes': request.POST.getlist('classe'), 'coefficient_Matiere': request.POST.get('coefficient_Matiere')})
            else:
                Classe_matiere.objects.filter(pk=request.POST.get('id')).update(
                    classe_m = classe,
                    matiere_c = matiere,
                    coefficient_Matiere = coefficient_Matiere
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse, 'msg': msg})
    else:
        return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})


@login_required(login_url="/login/")
def deleteCoefMatiereClasse(request):
    """
    Cette fonction permet de désactiver et d'activer un coefficient
    """
    template_name = 'Paramètre/listMatière/affecterCoefMatiereClasse.html'
    listMatiere = Matiere.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    listCoefMatiereClasse = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        classe_matiereQuery = Classe_matiere.objects.filter(pk=request.POST.get('id'))

        if classe_matiereQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                classe_matiereQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})
            elif request.POST.get('is_active') == 'False':
                classe_matiereQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})
    else:
        return render(request, template_name, {'listMatiere': listMatiere, 'listClasse': listClasse, 'listCoefMatiereClasse': listCoefMatiereClasse})

