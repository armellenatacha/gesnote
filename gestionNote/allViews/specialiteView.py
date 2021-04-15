from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def specialiteList(request):
    
    template_name = 'Paramètre/listSpecialite/listSpecialite.html'
    listSpecialite = Specialite.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        specialite = Specialite.objects.filter(nom_Specialite=request.POST.get('nom_Specialite'), is_active=True)
        if not specialite:
            # Ici on
            classes = request.POST.getlist('classe')
            specialite = Specialite()
            specialite.codeSpecialite = request.POST.get('codeSpecialite').lower()
            specialite.nom_Specialite = request.POST.get('nom_Specialite').lower()
            # specialite.is_staff = False
            specialite.save()

            if(classes):
                for classe in classes:
                    specialite.classe.add(Classe.objects.get(pk=classe))

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listSpecialite': listSpecialite, 'listClasse': listClasse, 'msg': msg})
        else:
            error = "Cet specialite existe déjà"
            return render(request, template_name, {'listSpecialite': listSpecialite, 'listClasse': listClasse, 'error': error, 'codeSpecialite': request.POST.get('codeSpecialite'), 'nom_Specialite': request.POST.get('nom_Specialite')})
    
    else:
        return render(request, template_name, {'listSpecialite': listSpecialite, 'listClasse': listClasse})


@login_required(login_url="/login/")
def specialiteUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listSpecialite/listSpecialite.html'
    listSpecialite = Specialite.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        specialiteQuery = Specialite.objects.filter(pk=request.POST.get('id'))

        codeSpecialite = request.POST.get('codeSpecialite')
        nom_Specialite = request.POST.get('nom_Specialite')

        if specialiteQuery:
            specialite = Specialite.objects.get(pk=request.POST.get('id'))
            classes = request.POST.getlist('classe')

            if Specialite.objects.filter(Q(codeSpecialite=codeSpecialite) & ~Q(pk=specialite.id)):
                error = "Impossible de modifier le code car: "+codeSpecialite+" existe déjà. Veuillez choisir un autre code"
                return render(request, template_name, {'error': error, 'codeSpecialite': codeSpecialite, 'nom_Specialite': nom_Specialite, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
            elif Specialite.objects.filter(Q(nom_Specialite=nom_Specialite) & ~Q(pk=specialite.id)):
                error = "Impossible de modifier le libelle car "+nom_Specialite+" est déjà lié à une matière.Veuillez choisir un autre libelle"
                return render(request, template_name, {'error': error, 'codeSpecialite': codeSpecialite, 'nom_Specialite': nom_Specialite, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
            else:
                Specialite.objects.filter(pk=request.POST.get('id')).update(
                    codeSpecialite = codeSpecialite,
                    nom_Specialite = nom_Specialite
                )
                if classes:
                    for classe in classes:
                        specialite.classe.add(classe)

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
    else:
        return render(request, template_name, {'listSpecialite': listSpecialite, 'listClasse': listClasse})


@login_required(login_url="/login/")
def specialiteDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listSpecialite/listSpecialite.html'
    listSpecialite = Specialite.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        specialiteQuery = Specialite.objects.filter(pk=request.POST.get('id'))

        if specialiteQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                specialiteQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
            elif request.POST.get('is_active') == 'False':
                specialiteQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listSpecialite': listSpecialite, 'listClasse': listClasse})
    else:
        return render(request, template_name, {'listSpecialite': listSpecialite, 'listClasse': listClasse})

