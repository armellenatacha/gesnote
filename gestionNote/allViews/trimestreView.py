from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def trimestreList(request):
    
    template_name = 'Paramètre/listTrimestre/listTrimestre.html'
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        trimestre = Trimestre.objects.filter(numero_trimestre=request.POST.get('numero_trimestre'), is_active=True)
        if not trimestre:
            # Ici on
            trimestre = Trimestre()
            trimestre.numero_trimestre = request.POST.get('numero_trimestre')
            # trimestre.is_staff = False
            trimestre.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listTrimestre': listTrimestre, 'msg': msg})
        else:
            error = "Ce trimestre existe déjà"
            return render(request, template_name, {'listTrimestre': listTrimestre, 'error': error, 'numero_trimestre': request.POST.get('numero_trimestre')})
    
    else:
        return render(request, template_name, {'listTrimestre': listTrimestre})


@login_required(login_url="/login/")
def trimestreUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listTrimestre/listTrimestre.html'
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        trimestreQuery = Trimestre.objects.filter(pk=request.POST.get('id'))

        numero_trimestre = request.POST.get('numero_trimestre')

        if trimestreQuery:
            trimestre = Trimestre.objects.get(pk=request.POST.get('id'))

            if Trimestre.objects.filter(Q(numero_trimestre=numero_trimestre) & ~Q(pk=trimestre.id)):
                error = "Impossible de modifier le libelle car "+numero_trimestre+" est déjà lié à une matière.Veuillez choisir un autre libelle"
                return render(request, template_name, {'error': error, 'numero_trimestre': numero_trimestre, 'listTrimestre': listTrimestre})
            else:
                Trimestre.objects.filter(pk=request.POST.get('id')).update(
                    numero_trimestre = numero_trimestre
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listTrimestre': listTrimestre})
    else:
        return render(request, template_name, {'listTrimestre': listTrimestre})


@login_required(login_url="/login/")
def trimestreDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listTrimestre/listTrimestre.html'
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        trimestreQuery = Trimestre.objects.filter(pk=request.POST.get('id'))

        if trimestreQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                trimestreQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listTrimestre': listTrimestre})
            elif request.POST.get('is_active') == 'False':
                trimestreQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listTrimestre': listTrimestre})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listTrimestre': listTrimestre})
    else:
        return render(request, template_name, {'listTrimestre': listTrimestre})

