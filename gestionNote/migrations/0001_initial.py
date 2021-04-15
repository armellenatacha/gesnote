# Generated by Django 3.1.7 on 2021-03-12 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nom', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('prenom', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(max_length=50, unique=True)),
                ('parent', models.BooleanField(default=False)),
                ('principal', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('chefInformatique', models.BooleanField(default=False)),
                ('professeur', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeClasse', models.CharField(max_length=200, verbose_name='codeClasse')),
                ('nom_classe', models.CharField(max_length=200, verbose_name='nom_classe')),
                ('niveau_classe', models.CharField(max_length=200, verbose_name='niveau_classe')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, unique=True)),
                ('prenom', models.CharField(blank=True, max_length=255, null=True)),
                ('matricule', models.CharField(blank=True, max_length=200, null=True, verbose_name='matricule')),
                ('date_naissance', models.DateTimeField(blank=True, null=True, verbose_name='date_naissance')),
                ('lieu_naissance', models.CharField(blank=True, max_length=200, null=True, verbose_name='lieu_naissance')),
                ('is_eleve', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeMatiere', models.CharField(max_length=200, verbose_name='codeMatiere')),
                ('nom_Matiere', models.CharField(max_length=200, verbose_name='nom_Matiere')),
                ('coefficient_Matiere', models.CharField(max_length=200, verbose_name='coefficient_Matiere')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Martiere',
                'verbose_name_plural': 'Martieres',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeModule', models.CharField(max_length=200, verbose_name='codeModule')),
                ('nom_module', models.CharField(max_length=200, verbose_name='nom_module')),
                ('coefficient_module', models.CharField(max_length=200, verbose_name='coefficient_module')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiereModule', to='gestionNote.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_trimestre', models.CharField(max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeSpecialite', models.CharField(max_length=200, verbose_name='codeSpecialite')),
                ('nom_Specialite', models.CharField(max_length=200, verbose_name='nom_Specialite')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classeSpec', to='gestionNote.classe')),
            ],
            options={
                'verbose_name': 'Specialite',
                'verbose_name_plural': 'Specialites',
            },
        ),
        migrations.CreateModel(
            name='Sequences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sequence', models.CharField(max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trimestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trimestreSeq', to='gestionNote.trimestre')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeResultat', models.CharField(max_length=200, verbose_name='codeResultat')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('eleveProfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleveResultat', to='gestionNote.eleve')),
                ('module', models.ManyToManyField(related_name='module', to='gestionNote.Modules')),
            ],
            options={
                'verbose_name': 'Resultat',
                'verbose_name_plural': 'Resultats',
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_professeur', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('professeurUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professeurUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_principal', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('principalUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='principalUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parentUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parentUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeNote', models.CharField(max_length=200, verbose_name='codeNote')),
                ('type_note', models.CharField(max_length=200, verbose_name='type_note')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleveNote', to='gestionNote.eleve')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiereNote', to='gestionNote.matiere')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.AddField(
            model_name='matiere',
            name='professeur',
            field=models.ManyToManyField(related_name='professeurMatiere', to='gestionNote.Professeur'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='parentEleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentEleve', to='gestionNote.parent'),
        ),
        migrations.AddField(
            model_name='classe',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleveClasse', to='gestionNote.eleve'),
        ),
        migrations.AddField(
            model_name='classe',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moduleClasse', to='gestionNote.modules'),
        ),
        migrations.CreateModel(
            name='ChefInformatique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_chef_informatique', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chef_informatique', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chef_informatique', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]