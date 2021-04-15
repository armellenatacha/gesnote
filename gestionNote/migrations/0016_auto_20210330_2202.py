# Generated by Django 3.1.7 on 2021-03-30 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNote', '0015_note_classe_n'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='prof_titulaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prof_titulaire', to='gestionNote.professeur'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='sexe',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='sexe'),
        ),
    ]
