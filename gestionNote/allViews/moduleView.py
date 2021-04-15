from __future__ import print_function

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *

from gestionNote.models import *

@login_required(login_url="/login/")
def moduleList(request):
    
    template_name = 'Paramètre/listModule/listModule.html'
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == 'POST':
        module = Modules.objects.filter(nom_module=request.POST.get('nom_module'), is_active=True)
        if not module:
            # Ici on
            module = Modules()
            module.codeModule = request.POST.get('codeModule').lower()
            module.nom_module = request.POST.get('nom_module').lower()
            # module.is_staff = False
            module.save()

            msg = "Opération effectuer avec succèss"
            return render(request, template_name, {'listModule': listModule, 'msg': msg})
        else:
            error = "Ce module existe déjà"
            return render(request, template_name, {'listModule': listModule, 'error': error, 'codeModule': request.POST.get('codeModule'), 'nom_module': request.POST.get('nom_module')})
    
    else:
        return render(request, template_name, {'listModule': listModule})


@login_required(login_url="/login/")
def moduleUpdate(request):
    """
    Cette fonction permet de modifier les informations du chef informatique
    """
    template_name = 'Paramètre/listModule/listModule.html'
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""
    if request.method == 'POST':
        moduleQuery = Modules.objects.filter(pk=request.POST.get('id'))

        codeModule = request.POST.get('codeModule')
        nom_module = request.POST.get('nom_module')

        if moduleQuery:
            module = Modules.objects.get(pk=request.POST.get('id'))

            if Modules.objects.filter(Q(codeModule=codeModule) & ~Q(pk=module.id)):
                error = "Impossible de modifier le code car: "+codeModule+" existe déjà. Veuillez choisir un autre code"
                return render(request, template_name, {'error': error, 'codeModule': codeModule, 'nom_module': nom_module, 'listModule': listModule})
            elif Modules.objects.filter(Q(nom_module=nom_module) & ~Q(pk=module.id)):
                error = "Impossible de modifier le libelle car "+nom_module+" est déjà lié à une matière.Veuillez choisir un autre libelle"
                return render(request, template_name, {'error': error, 'codeModule': codeModule, 'nom_module': nom_module, 'listModule': listModule})
            else:
                Modules.objects.filter(pk=request.POST.get('id')).update(
                    codeModule = codeModule,
                    nom_module = nom_module
                )

                msg = "Opération effectuer avec succèss"
                return render(request, template_name, {'msg': msg, 'listModule': listModule})
    else:
        return render(request, template_name, {'listModule': listModule})


@login_required(login_url="/login/")
def moduleDelete(request):
    """
    Cette fonction permet de désactiver et d'activer un chef informatique
    """
    template_name = 'Paramètre/listModule/listModule.html'
    listModule = Modules.objects.filter(is_active=True)
    msg = ""
    error = ""

    if request.method == "POST":

        moduleQuery = Modules.objects.filter(pk=request.POST.get('id'))

        if moduleQuery:
            # activer ou suspendre un chef informatique
            if request.POST.get('is_active') == 'True':
                moduleQuery.update(is_active=True)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listModule': listModule})
            elif request.POST.get('is_active') == 'False':
                moduleQuery.update(is_active=False)
                msg = "Opération effectué avec succèss"

                return render(request, template_name, {'msg': msg, 'listModule': listModule})
        else:
            error = "Erreur de suppression"
            return render(request, template_name, {'error': error, 'listModule': listModule})
    else:
        return render(request, template_name, {'listModule': listModule})

