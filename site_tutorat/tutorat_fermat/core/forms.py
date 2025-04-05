from django import forms
from django.forms import ModelForm, fields
from .models import Cours, CustomUser

#Formulaire pour reserver un cours
class ReservationForm(ModelForm):
    role = forms.ChoiceField(
        choices=[
            ('eleve', 'Élève'),
            ('tuteur', 'Tuteur'),
        ],
        label="Role",
        widget=forms.RadioSelect(attrs={'class': 'inline-radio'})
    )
    nom_matiere = forms.ChoiceField(choices=Cours.MATIERES, label="Matière", widget=forms.Select(attrs={'class': 'nom-matiere'}))
    niveau = forms.ChoiceField(choices=Cours.NIVEAUX, label="Niveau", widget=forms.Select(attrs={'class': 'niveau-form'}))

    #Selection de 3 dates ou le cours peut avoir lieu, 1 cours = 3 dates possibles
    date1 = fields.DateField(label="Date 1", widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-form'}))
    heure1 = forms.ChoiceField(
        label="Heure 1",
        choices=[(f"{h}:00", f"{h}:00") for h in range(8, 18)],
        widget=forms.Select(attrs={'class': 'heure-form'})
    )


    date2 = fields.DateField(label="Date 2", widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-form'}))
    heure2 = forms.ChoiceField(
        label="Heure 2",
        choices=[(f"{h}:00", f"{h}:00") for h in range(8, 18)],
        widget=forms.Select(attrs={'class': 'heure-form'})
    )


    date3 = fields.DateField(label="Date 3", widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-form'}))
    heure3 = forms.ChoiceField(
        label="Heure 3",
        choices=[(f"{h}:00", f"{h}:00") for h in range(8, 18)],
        widget=forms.Select(attrs={'class': 'heure-form'})
    )

    

    class Meta:
        model = Cours
        fields = ['role', 'nom_matiere', 'niveau', 'date1', 'heure1', 'date2', 'heure2', 'date3', 'heure3']

#Formulaire de creation d'un utilisateur
class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label="Prénom", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Nom", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    classe = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ['last_name', 'first_name','username', 'password', 'email', 'classe']