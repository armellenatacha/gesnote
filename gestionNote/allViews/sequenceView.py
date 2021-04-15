from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def sequenceList(request):
    
    template_name = 'Paramètre/listSequence/listSequence.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        sequence = Sequences.objects.filter(numero_sequence=request.POST.get('numero_sequence'), is_active=True)
        if not sequence:
            # Ici on
            sequence = Sequences()
            sequence.numero_sequence = request.POST.get('numero_sequence')
            sequence.trimestre = Trimestre.objects.get(pk=request.POST.get('trimestre'))
            # sequence.is_staff = False
            sequence.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listSequence': listSequence, 'listTrimestre': listTrimestre, 'msg': msg})
        else:
            error = "Cet sequence existe déjà"
            return render(request, template_name, {'listSequence': listSequence, 'listTrimestre': listTrimestre, 'error': error, 'numero_sequence': request.POST.get('numero_sequence')})
    
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listTrimestre': listTrimestre})


@login_required(login_url="/login/")
def sequenceUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listSequence/listSequence.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        sequenceQuery = Sequences.objects.filter(pk=request.POST.get('id'))

        numero_sequence = request.POST.get('numero_sequence')

        if sequenceQuery:
            sequence = Sequences.objects.get(pk=request.POST.get('id'))

            if Sequences.objects.filter(Q(numero_sequence=numero_sequence) & ~Q(pk=sequence.id)):
                error = "Impossible de modifier le libelle car "+numero_sequence+" est déjà lié à une matière.Veuillez choisir un autre libelle"
                return render(request, template_name, {'error': error, 'numero_sequence': numero_sequence, 'listSequence': listSequence})
            else:
                Sequences.objects.filter(pk=request.POST.get('id')).update(
                    numero_sequence = numero_sequence,
                    trimestre = Trimestre.objects.get(pk=request.POST.get('trimestre'))
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listTrimestre': listTrimestre})
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listTrimestre': listTrimestre})


@login_required(login_url="/login/")
def sequenceDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listSequence/listSequence.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listTrimestre = Trimestre.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        sequenceQuery = Sequences.objects.filter(pk=request.POST.get('id'))

        if sequenceQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                sequenceQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listTrimestre': listTrimestre})
            elif request.POST.get('is_active') == 'False':
                sequenceQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listTrimestre': listTrimestre})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listSequence': listSequence, 'listTrimestre': listTrimestre})
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listTrimestre': listTrimestre})

