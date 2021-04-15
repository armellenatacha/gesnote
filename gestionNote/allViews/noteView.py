from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

def tri_selection(notes):
    
    for i in range(len(notes)):
        max = i
        
        for j in range(i+1, len(notes)):
            if float(notes[max].codeNote) < float(notes[j].codeNote):
                max = j
                    
        tmp = notes[i]
        notes[i] = notes[max]
        notes[max] = tmp

    return notes

def tri_selection_trim(notes):
    for i in range(len(notes)):
        max = i
        
        for j in range(i+1, len(notes)):
            if float(notes[max]['codeNote']) < float(notes[j]['codeNote']):
                max = j
                  
        tmp = notes[i]
        notes[i] = notes[max]
        notes[max] = tmp
    return notes
    

def calculRang(matiere, classe, sequence, eleve):
    notes = Note.objects.filter(sequence=sequence, matiere=matiere, classe_n=classe)
    tab = list()
    count = 0

    for note in notes:
        tab.append(note)

    tri_selection(tab)

    for note in tab:
        count += 1
        if note.eleve == eleve:
            break
    
    return count
    

def calculRangTrim(matiere, classe, trimestre, eleve):
    
    if trimestre.numero_trimestre == "1":
        notes1 = Note.objects.filter(sequence=1, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=2, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "2":
        notes1 = Note.objects.filter(sequence=3, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=4, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "3":
        notes1 = Note.objects.filter(sequence=5, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=6, matiere=matiere, classe_n=classe)
    else:
        notes1 = []
        notes2 = []
    tab = list()
    trim = dict()
    count = 0
    i = 0

    for note1 in notes1:
        trim = {}
        for note2 in notes2:
            if note1.eleve.id == note2.eleve.id:
                trim['eleve'] = note1.eleve
                trim['codeNote'] = (float(note1.codeNote) + float(note2.codeNote))/2
                tab.append(trim)

    tri_selection_trim(tab)

    for note in tab:
        count += 1
        if note['eleve'] == eleve:
            break
    
    return count

def min_note(matiere, classe, sequence):
    notes = Note.objects.filter(sequence=sequence, matiere=matiere, classe_n=classe)
    tab = list()
    count = 0

    for note in notes:
        tab.append(note)
        count += 1
    tri_selection(tab)

    return float(tab[count-1].codeNote)

def moy_note(matiere, classe, sequence):
    notes = Note.objects.filter(sequence=sequence, matiere=matiere, classe_n=classe)
    moy = 0
    for note in notes:
        moy += float(note.codeNote)

    

    return moy/len(notes)

def max_note(matiere, classe, sequence):
    notes = Note.objects.filter(sequence=sequence, matiere=matiere, classe_n=classe)
    tab = list()

    for note in notes:
        tab.append(note)
    tri_selection(tab)

    return tab[0].codeNote

def min_note_trim(matiere, classe, trimestre):
    if trimestre.numero_trimestre == "1":
        notes1 = Note.objects.filter(sequence=1, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=2, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "2":
        notes1 = Note.objects.filter(sequence=3, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=4, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "3":
        notes1 = Note.objects.filter(sequence=5, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=6, matiere=matiere, classe_n=classe)
    else:
        notes1 = []
        notes2 = []
    tab = list()
    trim = dict()
    count = 0

    for note1 in notes1:
        trim = {}
        for note2 in notes2:
            if note1.eleve.id == note2.eleve.id:
                trim['eleve'] = note1.eleve
                trim['codeNote'] = (float(note1.codeNote) + float(note2.codeNote))/2
                tab.append(trim)
                count += 1
    tri_selection_trim(tab)
    return float(tab[count-1]['codeNote'])

def moy_note_trim(matiere, classe, trimestre):
    
    if trimestre.numero_trimestre == "1":
        notes1 = Note.objects.filter(sequence=1, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=2, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "2":
        notes1 = Note.objects.filter(sequence=3, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=4, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "3":
        notes1 = Note.objects.filter(sequence=5, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=6, matiere=matiere, classe_n=classe)
    else:
        notes1 = []
        notes2 = []
    moy = 0

    for note1 in notes1:
        for note2 in notes2:
            if note1.eleve.id == note2.eleve.id:
                moy += (float(note1.codeNote) + float(note2.codeNote))/2

    

    return moy/len(notes2)

def max_note_trim(matiere, classe, trimestre):
    
    if trimestre.numero_trimestre == "1":
        notes1 = Note.objects.filter(sequence=1, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=2, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "2":
        notes1 = Note.objects.filter(sequence=3, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=4, matiere=matiere, classe_n=classe)
    elif trimestre.numero_trimestre == "3":
        notes1 = Note.objects.filter(sequence=5, matiere=matiere, classe_n=classe)
        notes2 = Note.objects.filter(sequence=6, matiere=matiere, classe_n=classe)
    else:
        notes1 = []
        notes2 = []
    tab = list()
    trim = dict()
    count = 0

    for note1 in notes1:
        trim = {}
        for note2 in notes2:
            if note1.eleve.id == note2.eleve.id:
                trim['eleve'] = note1.eleve
                trim['codeNote'] = (float(note1.codeNote) + float(note2.codeNote))/2
                tab.append(trim)
                count += 1
    tri_selection_trim(tab)

    return tab[0]['codeNote']

def calRangGen(classe, sequence, currentEleve, matieres_coef):
    temp = dict()
    tab = list()
    tcoef = 0.0
    tNote = 0.0
    listEleve = Eleve.objects.filter(classe=classe)
    count = 0

    for eleve in listEleve:
        listNote = Note.objects.filter(eleve=eleve, sequence=sequence)
        temp = {}
        temp['eleve'] = eleve
        tNote = 0.0
        tcoef = 0.0
        for note in listNote:
            for coef in matieres_coef:
                if coef.matiere_c.id == note.matiere.id:
                    tcoef += float(coef.coefficient_Matiere)
                    tNote += float(note.codeNote) * float(coef.coefficient_Matiere)
        if tcoef != 0:
            temp['moy'] = tNote/tcoef
        else:
            temp['moy'] = 0
        tab.append(temp)

    for i in range(len(tab)):
        max = i
        
        for j in range(i+1, len(tab)):
            if float(tab[max]['moy']) < float(tab[j]['moy']):
                max = j
                    
        tmp = tab[i]
        tab[i] = tab[max]
        tab[max] = tmp

    for t in tab:
        count += 1
        if t['eleve'].id == currentEleve.id:
            break

    return count

def calMoyClasse(classe, sequence, matieres_coef):
    temp = dict()
    tab = list()
    tcoef = 0.0
    tNote = 0.0
    listEleve = Eleve.objects.filter(classe=classe)
    count = 0
    televe = 0

    for eleve in listEleve:
        televe += 1
        listNote = Note.objects.filter(eleve=eleve, sequence=sequence, classe_n=classe)
        temp = {}
        temp['eleve'] = eleve
        for note in listNote:
            for coef in matieres_coef:
                if coef.matiere_c.id == note.matiere.id:
                    tcoef += int(coef.coefficient_Matiere)
                    tNote += float(note.codeNote) * float(coef.coefficient_Matiere)
        if tcoef != 0:
            temp['moy'] = tNote/tcoef
        else:
            temp['moy'] = 0
        tab.append(temp)

    for t in tab:
        count += float(t['moy'])

    return float(count/televe)

def calRangGenTrim(classe, trimestre, currentEleve, matieres_coef):
    temp = dict()
    tab = list()
    tcoef = 0.0
    tNote = 0.0
    listEleve = Eleve.objects.filter(classe=classe)
    count = 0

    for eleve in listEleve:
        if trimestre.numero_trimestre == "1":
            listNote1 = Note.objects.filter(sequence=1, eleve=eleve)
            listNote2 = Note.objects.filter(sequence=2, eleve=eleve)
        elif trimestre.numero_trimestre == "2":
            listNote1 = Note.objects.filter(sequence=3, eleve=eleve)
            listNote2 = Note.objects.filter(sequence=4, eleve=eleve)
        elif trimestre.numero_trimestre == "3":
            listNote1 = Note.objects.filter(sequence=5, eleve=eleve)
            listNote2 = Note.objects.filter(sequence=6, eleve=eleve)
        else:
            listNote1 = []
            listNote2 = []
        temp = {}
        temp['eleve'] = eleve
        tNote = 0.0
        tcoef = 0.0
        for note1 in listNote1:
            for note2 in listNote2:
                if note1.matiere.id == note2.matiere.id:
                    for coef in matieres_coef:
                        if coef.matiere_c.id == note1.matiere.id:
                            tcoef += float(coef.coefficient_Matiere)
                            tNote += ((float(note1.codeNote) + float(note2.codeNote))/2) * float(coef.coefficient_Matiere)
        if tcoef != 0:
            temp['moy'] = tNote/tcoef
        else:
            temp['moy'] = 0
        tab.append(temp)

    for i in range(len(tab)):
        max = i
        
        for j in range(i+1, len(tab)):
            if float(tab[max]['moy']) < float(tab[j]['moy']):
                max = j
                    
        tmp = tab[i]
        tab[i] = tab[max]
        tab[max] = tmp

    for t in tab:
        count += 1
        if t['eleve'].id == currentEleve.id:
            break

    return count

def calMoyTrim(classe, trimestre, currentEleve, matieres_coef):
    temp = dict()
    tab = list()
    tcoef = 0.0
    tNote = 0.0
    count = 0

    if trimestre.numero_trimestre == "1":
        listNote1 = Note.objects.filter(sequence=1, eleve=currentEleve)
        listNote2 = Note.objects.filter(sequence=2, eleve=currentEleve)
    elif trimestre.numero_trimestre == "2":
        listNote1 = Note.objects.filter(sequence=3, eleve=currentEleve)
        listNote2 = Note.objects.filter(sequence=4, eleve=currentEleve)
    elif trimestre.numero_trimestre == "3":
        listNote1 = Note.objects.filter(sequence=5, eleve=currentEleve)
        listNote2 = Note.objects.filter(sequence=6, eleve=currentEleve)
    else:
        listNote1 = []
        listNote2 = []
    temp = {}
    temp['eleve'] = eleve
    tNote = 0.0
    tcoef = 0.0
    for note1 in listNote1:
        for note2 in listNote2:
            if note1.matiere.id == note2.matiere.id:
                for coef in matieres_coef:
                    if coef.matiere_c.id == note1.matiere.id:
                        tcoef += float(coef.coefficient_Matiere)
                        tNote += (float(note1.codeNote) + float(note2.codeNote)) * float(coef.coefficient_Matiere)
    if tcoef != 0:
        temp['moy'] = tNote/tcoef
    else:
        temp['moy'] = 0

    return tNote/tcoef

def calMoyClasseTrim(classe, trimestre, matieres_coef):
    temp = dict()
    tab = list()
    tcoef = 0.0
    tNote = 0.0
    listEleve = Eleve.objects.filter(classe=classe)
    count = 0
    televe = 0

    for eleve in listEleve:
        televe += 1
        if trimestre.numero_trimestre == "1":
            listNote1 = Note.objects.filter(sequence=1, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=2, eleve=eleve, classe_n=classe)
        elif trimestre.numero_trimestre == "2":
            listNote1 = Note.objects.filter(sequence=3, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=4, eleve=eleve, classe_n=classe)
        elif trimestre.numero_trimestre == "3":
            listNote1 = Note.objects.filter(sequence=5, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=6, eleve=eleve, classe_n=classe)
        else:
            listNote1 = []
            listNote2 = []
        temp = {}
        temp['eleve'] = eleve
        for note1 in listNote1:
            for note2 in listNote2:
                if note1.matiere.id == note2.matiere.id:
                    for coef in matieres_coef:
                        if coef.matiere_c.id == note1.matiere.id:
                            tcoef += int(coef.coefficient_Matiere)
                            tNote += ((float(note1.codeNote) + float(note2.codeNote))/2) * int(coef.coefficient_Matiere)
        if tcoef != 0:
            temp['moy'] = tNote/tcoef
        else:
            temp['moy'] = 0
        tab.append(temp)

    for t in tab:
        count += float(t['moy'])

    return float(count/televe)

            

@login_required(login_url="/login/")
def enregistrerNote(request):
    
    template_name = 'operation/enregistrerNote/enregistrerNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    # listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        
        listNote = request.POST.getlist('note')
        listEleve = request.POST.getlist('idEleve')
        compt = 0
        if listNote:
            for note_el in listNote:
                # Ici on
                print(request.POST.get('idEleve'))
                note = Note()
                note.codeNote = note_el
                note.sequence = Sequences.objects.get(pk=request.POST.get('sequence'))
                note.matiere = Matiere.objects.get(pk=request.POST.get('matiere'))
                note.classe_n = Classe.objects.get(pk=request.POST.get('classe'))
                note.eleve = Eleve.objects.get(pk=listEleve[compt])
                # note.is_staff = False
                note.save()
                compt += 1

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})
        else:
            error = "Erreur d'enregistrement des note"
            return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'error': error})
    
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})


@login_required(login_url="/login/")
def noteUpdate(request):
    
    template_name = 'operation/modifierNote/modifierNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    # listMatiere = Matiere.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        noteQuery = Note.objects.filter(pk=request.POST.get('id'))

        listIdNote = request.POST.getlist('idNote')
        listNote = request.POST.getlist('note')
        compt = 0

        print(compt)

        for note in listIdNote:
            noteQuery = Note.objects.filter(pk=note)

            if noteQuery:
                notee = Note.objects.get(pk=note)

                Note.objects.filter(pk=note).update(
                    codeNote = listNote[compt]
                )

                compt += 1

        msg = "Opération effectuer avec succèss"
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})
    else:
        return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse, 'msg': msg})

@login_required(login_url="/login/")
def showNote(request):
    
    template_name = 'operation/showNote/showNote.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})

@login_required(login_url="/login/")
def showNoteParent(request):
    
    template_name = 'resultat/monEnfant/monEnfant.html'
    listSequence = Sequences.objects.filter(is_active=True)
    listClasse = Classe.objects.filter(is_active=True)
    return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})

@login_required(login_url="/login/")
def showBulletin(request):
    template_name = 'PV/Bulletin/bulletin.html'
    return render(request, template_name)

@login_required(login_url="/login/")
def showBulletinSequentiel(request):
    templare_name = 'resultat/bulletinSequentielle/bulletinSeq.html'
    f = 0
    g = 0
    t = 0
    bulletin = dict()
    bulletin_module = dict()
    table = list()
    table_module = list()
    temp_note = 0
    temp_coef = 0
    temp_coef_note = 0
    total_point = 0
    total_coef = 0
    moy = 0
    nbr_matiere = 0
    tableau_honneur = ''

    if request.method == 'POST':
        sequence = Sequences.objects.get(numero_sequence=request.POST.get('idSeq'))
        eleve = Eleve.objects.get(pk=request.POST.get('idEleve'))
        classe = Classe.objects.get(pk=request.POST.get('idClasse'))
        matieres_coef = Classe_matiere.objects.filter(classe_m=classe)
        modules = classe.module.all()
        prof_titulaire = classe.prof_titulaire

        listNote = Note.objects.filter(sequence=sequence, eleve=eleve, classe_n=classe)

        listEleve = Eleve.objects.filter(classe=classe, is_active=True)
        for e in listEleve:
            if e.sexe == 'feminin':
                f += 1
                t += 1
            elif e.sexe == 'masculin':
                g += 1
                t += 1

        for module in modules:
            temp_note = 0
            temp_coef = 0
            temp_coef_note = 0
            bulletin_module = {}
            for note in listNote:
                bulletin = {}
                if note.matiere.module.id == module.id:
                    bulletin['module'] = module.nom_module
                    bulletin['matiere'] = note.matiere.nom_Matiere
                    nbr_matiere += 1
                    bulletin['note'] = note.codeNote
                    temp_note += float(bulletin['note'])
                    for coef in matieres_coef:
                       if coef.matiere_c.id == note.matiere.id:
                           bulletin['coef'] = coef.coefficient_Matiere
                           temp_coef += int(bulletin['coef'])
                           total_coef += int(bulletin['coef'])
                           bulletin['noteCoef'] = float(note.codeNote) * float(coef.coefficient_Matiere)
                           total_point += float(note.codeNote) * float(coef.coefficient_Matiere)
                           temp_coef_note += float(bulletin['noteCoef'])
                           bulletin['rang'] = calculRang(note.matiere, classe, sequence, eleve)
                           bulletin['min'] = min_note(note.matiere, classe, sequence)
                           bulletin['moy'] = moy_note(note.matiere, classe, sequence)
                           bulletin['max'] = max_note(note.matiere, classe, sequence)
                           for prof in note.matiere.professeur.all():
                                bulletin['prof'] = prof.professeurUser.nom +" "+ prof.professeurUser.prenom 
                table.append(bulletin)
            bulletin_module['nom_module'] = module.nom_module
            bulletin_module['note'] = temp_note
            bulletin_module['coef'] = temp_coef
            bulletin_module['noteCoef'] = temp_coef_note
            if temp_coef != 0:
                bulletin_module['moy_module'] = temp_coef_note / temp_coef
            else:
                bulletin_module['moy_module'] = 0
            table_module.append(bulletin_module)
        if total_coef != 0:
            moy = total_point/total_coef
        else:
            moy = 0
        rang = calRangGen(classe, sequence, eleve, matieres_coef)
        moyClasse = calMoyClasse(classe, sequence, matieres_coef)

        if moy >= 12:
            tableau_honneur = 'OUI'
        else:
            tableau_honneur = 'NON'


        return render(request, templare_name, {'tableau_honneur': tableau_honneur, 'moyClasse': moyClasse, 'rang': rang, 'total_point': total_point, 'total_coef': total_coef, 'moy': moy, 'nbr_matiere': nbr_matiere, 'tables': table, 'table_modules': table_module, 'sequence': sequence, 'matieres_coef': matieres_coef, 'modules': modules, 'listNote': listNote, 'classe': classe, 'eleve': eleve, 'f': f, 'g': g, 't': t})

@login_required(login_url="/login/")
def showBulletinTrimestrielle(request):
    templare_name = 'resultat/bulletinTrimestrielle/bulletinTrim.html'
    f = 0
    g = 0
    t = 0
    bulletin = dict()
    bulletin_module = dict()
    table = list()
    table_module = list()
    temp_note = 0
    temp_coef = 0
    temp_coef_note = 0
    total_point = 0
    total_coef = 0
    moy = 0
    nbr_matiere = 0
    tableau_honneur = ''
    seq1 = 0
    seq2 = 0
    temp_note_s1 = 0
    temp_note_s2 = 0

    if request.method == 'POST':
        trimestre = Trimestre.objects.get(numero_trimestre=request.POST.get('idTrim'))
        eleve = Eleve.objects.get(pk=request.POST.get('idEleve'))
        classe = Classe.objects.get(pk=request.POST.get('idClasse'))
        matieres_coef = Classe_matiere.objects.filter(classe_m=classe)
        modules = classe.module.all()
        prof_titulaire = classe.prof_titulaire
        if trimestre.numero_trimestre == "1":
            print('seq 1')
            listNote1 = Note.objects.filter(sequence=1, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=2, eleve=eleve, classe_n=classe)
            seq1 = 1
            seq2 = 2
        elif trimestre.numero_trimestre == "2":
            print('seq 2')
            listNote1 = Note.objects.filter(sequence=3, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=4, eleve=eleve, classe_n=classe)
            seq1 = 3
            seq2 = 4
        elif trimestre.numero_trimestre == "3":
            print('seq 3')
            listNote1 = Note.objects.filter(sequence=5, eleve=eleve, classe_n=classe)
            listNote2 = Note.objects.filter(sequence=6, eleve=eleve, classe_n=classe)
            seq1 = 5
            seq2 = 6
        else:
            print('seq 0')
            listNote1 = []
            listNote2 = []
            

        listEleve = Eleve.objects.filter(classe=classe, is_active=True)
        for e in listEleve:
            if e.sexe == 'feminin':
                f += 1
                t += 1
            elif e.sexe == 'masculin':
                g += 1
                t += 1

        for module in modules:
            temp_note_s1 = 0
            temp_note_s2 = 0
            temp_note = 0
            temp_coef = 0
            temp_coef_note = 0
            bulletin_module = {}
            i = 0
            for note1 in listNote1:
                for note2 in listNote2:
                    bulletin = {}
                    if note1.matiere.module.id == module.id and note2.matiere.id == note1.matiere.id:
                        print(note1.codeNote)
                        print("---------------------------------------------------")
                        print(note2.codeNote)
                        bulletin['module'] = module.nom_module
                        bulletin['matiere'] = note1.matiere.nom_Matiere
                        nbr_matiere += 1
                        bulletin['t1s1'] = note1.codeNote
                        temp_note_s1 += float(bulletin['t1s1'])
                        bulletin['t1s2'] = note2.codeNote
                        temp_note_s2 += float(bulletin['t1s2'])
                        bulletin['note'] = (float(bulletin['t1s1']) + float(bulletin['t1s2']))/2
                        temp_note += float(bulletin['note'])
                        for coef in matieres_coef:
                            if coef.matiere_c.id == note1.matiere.id:
                                bulletin['coef'] = coef.coefficient_Matiere
                                temp_coef += int(bulletin['coef'])
                                total_coef += int(bulletin['coef'])
                                bulletin['noteCoef'] = float(bulletin['note']) * float(coef.coefficient_Matiere)
                                total_point += float(bulletin['note']) * float(coef.coefficient_Matiere)
                                temp_coef_note += float(bulletin['noteCoef'])
                                bulletin['rang'] = calculRangTrim(note1.matiere, classe, trimestre, eleve)
                                bulletin['min'] = min_note_trim(note1.matiere, classe, trimestre)
                                bulletin['moy'] = moy_note_trim(note1.matiere, classe, trimestre)
                                bulletin['max'] = max_note_trim(note1.matiere, classe, trimestre)
                                for prof in note1.matiere.professeur.all():
                                        bulletin['prof'] = prof.professeurUser.nom +" "+ prof.professeurUser.prenom 
                    table.append(bulletin)
                    i += 1
            bulletin_module['nom_module'] = module.nom_module
            bulletin_module['t1s1'] = temp_note_s1
            bulletin_module['t1s2'] = temp_note_s2
            bulletin_module['note'] = temp_note
            bulletin_module['coef'] = temp_coef
            bulletin_module['noteCoef'] = temp_coef_note
            if temp_coef != 0:
                bulletin_module['moy_module'] = temp_coef_note / temp_coef
            else:
                bulletin_module['moy_module'] = 0
            table_module.append(bulletin_module)
        if total_coef != 0:
            moy = total_point/total_coef
        else:
            moy = 0
        rang = calRangGenTrim(classe, trimestre, eleve, matieres_coef)
        moyClasse = calMoyClasseTrim(classe, trimestre, matieres_coef)

        if moy >= 12:
            tableau_honneur = 'OUI'
        else:
            tableau_honneur = 'NON'

        if trimestre.numero_trimestre == "1":
            print('seq 1')
            moy1 = 0
            moy2 = 0
        elif trimestre.numero_trimestre == "2":
            print('seq 2')
            moy1 = calMoyTrim(classe, Trimestre.objects.get(numero_trimestre="1"), eleve, matieres_coef)
            moy2 = 0
        elif trimestre.numero_trimestre == "3":
            print('seq 3')
            moy1 = calMoyTrim(classe, Trimestre.objects.get(numero_trimestre="1"), eleve, matieres_coef)
            moy2 = calMoyTrim(classe, Trimestre.objects.get(numero_trimestre="2"), eleve, matieres_coef)
        else:
            print('seq 0')
            moy1 = 0
            moy2 = 0

        annuelle = (moy + moy1 + moy2)/3
            


        return render(request, templare_name, {'annuelle': annuelle, 'moy1': moy1, 'moy2': moy2, 'seq1': seq1,'seq2': seq2,'temp_note_s1': temp_note_s1,'temp_note_s2': temp_note_s2,'tableau_honneur': tableau_honneur, 'moyClasse': moyClasse, 'rang': rang, 'total_point': total_point, 'total_coef': total_coef, 'moy': moy, 'nbr_matiere': nbr_matiere, 'tables': table, 'table_modules': table_module, 'trimestre': trimestre, 'matieres_coef': matieres_coef, 'modules': modules, 'classe': classe, 'eleve': eleve, 'f': f, 'g': g, 't': t})



# @login_required(login_url="/login/")
# def sequenceDelete(request):
#     """
#     Cette fonction permet de désactiver et d'activer un chef informatique
#     """
#     template_name = 'Paramètre/listSequence/listSequence.html'
#     listSequence = Note.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     listClasse = Classe.objects.filter(is_active=True)
#     msg = ""
#     error = ""

#     if request.method == "POST":

#         noteQuery = Note.objects.filter(pk=request.POST.get('id'))

#         if noteQuery:
#             # activer ou suspendre un chef informatique
#             if request.POST.get('is_active') == 'True':
#                 noteQuery.update(is_active=True)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#             elif request.POST.get('is_active') == 'False':
#                 noteQuery.update(is_active=False)
#                 msg = "Opération effectué avec succèss"

#                 return render(request, template_name, {'msg': msg, 'listSequence': listSequence, 'listClasse': listClasse})
#         else:
#             error = "Erreur de suppression"
#             return render(request, template_name, {'error': error, 'listSequence': listSequence, 'listClasse': listClasse})
#     else:
#         return render(request, template_name, {'listSequence': listSequence, 'listClasse': listClasse})

