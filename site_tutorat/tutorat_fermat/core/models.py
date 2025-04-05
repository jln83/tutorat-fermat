from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cours(models.Model):
    MATIERES = [
        ('maths', 'Maths'),
        ('physique', 'Physique'),
        ('chimie', 'Chimie'),
        ('maths_experts', 'Maths expertes'),
        ('maths_complementaires', 'Maths complémentaires'),
        ('anglais', 'Anglais'),
        ('francais', 'Français'),
        ('nsi', 'NSI'),
        ('philosophie', 'Philosophie'),
        ('svt', 'SVT'),
        ('histoire', 'Histoire'),
        ('geographie', 'Géographie'),
        ('ses', 'SES'),
        ('si', 'SI'),
        ('espagnol', 'Espagnol'),
        ('allemand', 'Allemand'),
        ('geopolitique', 'Géopolitique (Geopo)'),
        ('hlp', 'HLP'),
        ('emc', 'EMC'),
        ('latin', 'Latin'),
        ('grec', 'Grec'),
        ('es_maths', 'ES Maths'),
        ('es_pc', 'ES PC'),
        ('es_svt', 'ES SVT'),
        ('arabe', 'Arabe'),
        ('italien', 'Italien'),
    ]

    NIVEAUX = [
        ('seconde', 'Seconde'),
        ('premiere', 'Première'),
        ('terminale', 'Terminale'),
    ]

    MONTHS = [
        ('janvier', 'Janvier'),
        ('fevrier', 'Février'),
        ('mars', 'Mars'),
        ('avril', 'Avril'),
        ('mai', 'Mai'),
        ('juin', 'Juin'),
        ('juillet', 'Juillet'),
        ('aout', 'Août'),
        ('septembre', 'Septembre'),
        ('octobre', 'Octobre'),
        ('novembre', 'Novembre'),
        ('decembre', 'Décembre'),
    ]

    ROLES = [
        ('eleve', 'Élève'),
        ('tuteur', 'Tuteur'),
    ]

    nom_matiere = models.CharField(max_length=50, choices=MATIERES)
    niveau = models.CharField(max_length=10, choices=NIVEAUX)

    date1 = models.DateField()
    heure1 = models.TimeField()

    date2 = models.DateField(default='2000-01-01')
    heure2 = models.TimeField(default='00:00:00')

    date3 = models.DateField(default='2000-01-01')
    heure3 = models.TimeField(default='00:00:00')

    role = models.CharField(max_length=20, choices=ROLES)

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)


class CustomUser(AbstractUser):
    num_tel = models.CharField(max_length=20, null=True, blank=True)
    classe = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.username