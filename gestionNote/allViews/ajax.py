from __future__ import print_function

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *
from gestionNote.models import *

@login_required(login_url="/login/")
def select_matiere(request):
    matieres = [];
    classe = Classe.objects.get(pk=request.GET.get('classe'))
    matiere_prof = Professeur.objects.get(professeurUser_id=request.user.id).professeurMatiere.all()

    for m in classe.classeMatiere.all():
        for c in matiere_prof:
            if (m.id == c.id):
                matieres.append(m)

                # matieres.

    return render(request, 'ajax/_choix_matiere.html', {'matieres': matieres})

@login_required(login_url="/login/")
def select_matiere_all(request):
    matieres = [];
    classe = Classe.objects.get(pk=request.GET.get('classe'))

    for m in classe.classeMatiere.all():
        matieres.append(m)

    return render(request, 'ajax/_choix_matiere.html', {'matieres': matieres})

@login_required(login_url="/login/")
def show_form(request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'))
    return render(request, 'ajax/_enregistrerNote.html', {'listEleve': eleves, 'sequence': request.GET.get('sequence'), 'classe': request.GET.get('classe'), 'matiere': request.GET.get('matiere')})

@login_required(login_url="/login/")
def show_form_update(request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'))
    notes = list()
    for eleve in eleves:
        print(eleve.id)
        notes.append(Note.objects.get(eleve_id=eleve.id, sequence_id=request.GET.get('sequence'), matiere_id=request.GET.get('matiere'), classe_n_id=request.GET.get('classe'), is_active=True))
        print(notes)
    return render(request, 'ajax/_modifierNote.html', {'listEleve': eleves, 'listNote': notes, 'sequence': request.GET.get('sequence'), 'classe': request.GET.get('classe'), 'matiere': request.GET.get('matiere')})

@login_required(login_url="/login/")
def show_table_note(request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'))
    notes = list()
    for eleve in eleves:
        print(eleve.id)
        notes.append(Note.objects.get(eleve_id=eleve.id, sequence_id=request.GET.get('sequence'), matiere_id=request.GET.get('matiere'), classe_n_id=request.GET.get('classe'), is_active=True))
        print(notes)
    return render(request, 'ajax/_showNote.html', {'listEleve': eleves, 'listNote': notes, 'sequence': request.GET.get('sequence'), 'classe': request.GET.get('classe'), 'matiere': request.GET.get('matiere')})

@login_required(login_url="/login/")
def show_table_note_enfant(request):
    notes = Note.objects.filter(sequence=request.GET.get('sequence'), classe_n=request.GET.get('classe'), eleve=request.GET.get('eleve'))
    return render(request, 'ajax/_showNoteEleveParent.html', {'listNote': notes})

@login_required(login_url="/login/")
def get_eleve_classe(request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'))

    return render(request, 'ajax/_listEleveBulSq.html', {'listEleve': eleves, 'idClasse': request.GET.get('classe')})

@login_required(login_url="/login/")
def get_eleve_classe_trim(request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'))

    return render(request, 'ajax/_listEleveBulTrim.html', {'listEleve': eleves, 'idClasse': request.GET.get('classe')})

@login_required(login_url="/login/")
def get_eleve_parent (request):
    eleves = Eleve.objects.filter(classe_id=request.GET.get('classe'), parentEleve=Parent.objects.get(parentUser=request.user.id))

    return render(request, 'ajax/_choix_eleve.html', {'eleves': eleves})
