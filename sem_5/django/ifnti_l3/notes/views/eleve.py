from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from notes.models import Eleve,Note
from notes.forms.EleveForm import EleveForm
from django.contrib.auth.decorators import login_required, permission_required








# Vue pour la liste des élèves avec leurs matières et moyennes
@login_required
@permission_required('notes.view_eleve', raise_exception=True)
def eleves(request):
    # Récupère tous les élèves depuis la base de données
    eleves_list = Eleve.objects.all()

    # Pour chaque élève, on récupère leurs notes et moyennes
    eleves_with_notes = []
    for eleve in eleves_list:
        matieres_notes = []
        # Récupérer les notes pour chaque matière de l'élève
        for matiere in eleve.matieres.all():
            note = Note.objects.filter(eleve=eleve, matiere=matiere).first()  # Récupère la note
            matieres_notes.append({
                'matiere': matiere.nom,
                'note': note.valeur if note else 'Nulle'  # Vérifie si une note existe
            })
        eleves_with_notes.append({
            "id": eleve.id,
            'nom': eleve.nom,
            "prenom" : eleve.prenom,
            "sexe" : eleve.sexe,
            "date_naissance" : eleve.date_naissance,
            "niveau_id": eleve.niveau.id,
            'niveau': eleve.niveau.nom,
            'matieres_notes': matieres_notes
        })
        

    # for eleves in eleves_with_notes:
    #     print(eleves)
    
    # return HttpResponse(eleves_with_notes)
    

    # Retourne le template avec la liste des élèves, leurs matières et moyennes
    return render(request, 'notes/eleves.html', {'eleves': eleves_with_notes})


@login_required  # Nécessite que l'utilisateur soit connecté
@permission_required('notes.view_eleve', raise_exception=True)
def eleve(request, id):
    detail_eleve = get_object_or_404(Eleve, id=id)
    matiere = detail_eleve.matieres.all()
    print(matiere)
    
    # for elev in detail_eleve:
    #     print(elev)
    # matieres_notes = []
    # for matiere in detail_eleve.matieres.all():
    #     # Récupérer la note pour chaque matière
    #     note = Note.objects.filter(eleve=detail_eleve, matiere=matiere).first()
    #     matieres_notes.append({
    #         'matiere': matiere.nom,
    #         'note': note.valeur if note else 'NULL'  # Si la note n'existe pas, afficher 'N/A'
    #     })
    
    return render(request, 'notes/detail_eleve.html', {
        # 'eleve_id':id,
        # 'matiere_id' : matiere.id,
        'eleve': detail_eleve,
        'matieres': matiere,
    })


@login_required  # Nécessite que l'utilisateur soit connecté
@permission_required('notes.add_eleve', raise_exception=True)
def add_eleve(request):
    form = EleveForm()  # Initialiser le formulaire

    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre l'élève dans la base de données
            
            # Redirige vers la vue de liste des élèves
            return redirect('notes:eleves')  # Remplacez 'notes:eleves' par le nom correct de votre URL

    return render(request, 'notes/add_eleve.html', {'form': form})


@login_required  # Nécessite que l'utilisateur soit connecté
@permission_required('notes.change_eleve', raise_exception=True) 
def update_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)  # Récupère l'élève par son identifiant
    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)  # Prend l'instance existante
        if form.is_valid():
            form.save()  # Enregistre les modifications
            return redirect('eleve_list')  # Redirige vers la liste des élèves
    else:
        form = EleveForm(instance=eleve)  # Préremplit le formulaire avec les données de l'élève
    
    return render(request, 'notes/update_eleve.html', {'form': form}) 




# Vue pour la liste des élèves avec leurs notes et moyennes
# def eleve(request):
#     liste_eleves = Eleve.objects.all()
#     return render(request, 'notes/eleves.html', {'eleves': liste_eleves})




# Vue pour le détail d'un élève particulier

    
    
    # return HttpResponse(detail_eleve,matieres_notes)






# def add_eleve(request):
#     form = EleveForm()  # Initialiser le formulaire en dehors du bloc if

#     if request.method == 'POST':
#         form = EleveForm(request.POST)
#         if form.is_valid():
#             form.save()  # Enregistre l'élève dans la base de données
            
#             # Récupère tous les élèves depuis la base de données
#             eleves_list = Eleve.objects.all()

#             # Pour chaque élève, on récupère leurs notes et moyennes
#             eleves_with_notes = []
#             for eleve in eleves_list:
#                 matieres_notes = []
#                 # Récupérer les notes pour chaque matière de l'élève
#                 for matiere in eleve.matieres.all():
#                     note = Note.objects.filter(eleve=eleve, matiere=matiere).first()  # Récupère la note
#                     matieres_notes.append({
#                         'matiere': matiere.nom,
#                         'note': note.valeur if note else 'Nulle'  # Vérifie si une note existe
#                     })
#                 eleves_with_notes.append({
#                     "id": eleve.id,
#                     'nom': eleve.nom,
#                     "prenom": eleve.prenom,
#                     "sexe": eleve.sexe,
#                     "date_naissance": eleve.date_naissance,
#                     "niveau_id": eleve.niveau.id,
#                     'niveau': eleve.niveau.nom,
#                     'matieres_notes': matieres_notes
#                 })

#             # Retourne le template avec la liste des élèves, leurs matières et moyennes
#             return render(request, 'notes/eleves.html', {'eleves': eleves_with_notes})
    
#     # Rendre le formulaire (déjà initialisé pour le cas GET)
#     return render(request, 'notes/add_eleve.html', {'form': form})










# def eleve(request):
#     eleves_list = Eleve.objects.all()
    
#     html_content = """
#     <html>
#         <head>
#             <title>Liste des élèves et leurs notes</title>
#         </head>
#         <body>
#             <h1>Liste des élèves et leurs notes</h1>
#             <table border="1">
#                 <thead>
#                     <tr>
#                         <th>Nom de l'élève</th>
#                         <th>Niveau</th>
#                         <th>Matière</th>
#                         <th>Note</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#     """

#     for eleve in eleves_list:
#         for matiere in eleve.matieres.all():
#             note = Note.objects.filter(eleve=eleve, matiere=matiere).first()
#             note_value = note.valeur if note else 'Nulle'
#             html_content += f"""
#                 <tr>
#                     <td>{eleve.nom}</td>
#                     <td>{eleve.niveau.nom}</td>
#                     <td>{matiere.nom}</td>
#                     <td>{note_value}</td>
#                 </tr>
#             """

#     # Fin du contenu HTML
#     html_content += """
#                 </tbody>
#             </table>
#         </body>
#     </html>
#     """

#     return HttpResponse(html_content)










# def eleves(request, id):
#     try:
#         # Récupérer l'élève manuellement
#         detail_eleve = Eleve.objects.get(id=id)
#     except Eleve.DoesNotExist:
#         # Si l'élève n'existe pas, renvoyer un message d'erreur simple
#         return HttpResponse("<h1>Élève non trouvé</h1>")
    
#     # Construire le contenu HTML
#     html_content = f"""
#     <html>
#         <head>
#             <title>Détails de l'élève</title>
#         </head>
#         <body>
#             <h1>Détails de l'élève : {detail_eleve.nom}</h1>
#             <h2>Niveau : {detail_eleve.niveau.nom}</h2>
#             <h3>Notes par matière</h3>
#             <table border="1">
#                 <thead>
#                     <tr>
#                         <th>Matière</th>
#                         <th>Note</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#     """
    
#     # Ajout des notes dans la table
#     for matiere in detail_eleve.matieres.all():
#         note = Note.objects.filter(eleve=detail_eleve, matiere=matiere).first()
#         note_value = note.valeur if note else 'Nulle'  # Si pas de note, mettre 'Nulle'
        
#         html_content += f"""
#             <tr>
#                 <td>{matiere.nom}</td>
#                 <td>{note_value}</td>
#             </tr>
#         """
    
#     # Fin du contenu HTML
#     html_content += """
#                 </tbody>
#             </table>
#         </body>
#     </html>
#     """
    
#     return HttpResponse(html_content)



