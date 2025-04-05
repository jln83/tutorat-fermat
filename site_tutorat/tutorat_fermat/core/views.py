from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ReservationForm, CustomUserCreationForm
from .models import Cours, CustomUser
from .services import find_compatible_tutor, find_compatible_student, send_email_match



def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seances')
        else:
            return render(request, 'login.html', {'error': "Mot de passe ou nom d'utilisateur invalide !"})
    return render(request, 'login.html')


def confidentialite(request):
    return render(request, 'confidentialite.html')


def creationdecompte(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            for i in form:
                print(i)
            form.save()
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    return render(request, 'create_account.html', {'form': CustomUserCreationForm()})


@login_required
def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserv = form.save(commit=False)
            reserv.user_id = request.user
            print(reserv.user_id)
            reserv.save()
            if reserv.role == 'eleve':
                student = reserv.user_id
                tutors = []
                for tutor in Cours.objects.filter(role='tuteur'):
                    tutors.append(tutor)
                tutor = find_compatible_tutor(reserv, tutors)
                if tutor is None:
                    print("Pas de match directmement trouve")
                else:
                    tutorUser = CustomUser.objects.get(id=tutor[0].user_id.id)
                    studentUser = CustomUser.objects.get(id=reserv.user_id.id)
                    with open('hist.txt', 'a') as f:
                        f.write(f"eleve: {tutor[0].user_id}, tuteur: {reserv.user_id}, cours: {reserv.nom_matiere}, date: {tutor[1]}, heure: {tutor[2]}\n")
                    print(f"{tutor[0].user_id} {tutorUser.first_name} {reserv.user_id} {studentUser.first_name} {reserv.nom_matiere} {tutor[1]} {tutor[2]}")
                    send_email_match(tutor[0].user_id.id, reserv.user_id.id, tutor[1], tutor[2], reserv)
                    tutor[0].delete()
                    reserv.delete()
            else:
                tutor = reserv.user_id
                students = []
                for student in Cours.objects.filter(role='eleve'):
                    students.append(student)
                student = find_compatible_student(reserv, students)
                if student is None:
                    print("Pas de match directmement trouve")
                else:
                    studentUser = CustomUser.objects.get(id=student[0].user_id.id)
                    tutorUser = CustomUser.objects.get(id=reserv.user_id.id)
                    with open('hist.txt', 'a') as f:
                        f.write(f"{reserv.user_id} {tutorUser.first_name} {student[0].user_id} {studentUser.first_name} {reserv.nom_matiere} {student[1]} {student[2]}\n")
                    print(f"Match trouve, eleve: {student[0].user_id}, tuteur: {reserv.user_id}, cours: {reserv.nom_matiere}, date: {student[1]}, heure: {student[2]}")
                    send_email_match(reserv.user_id.id, student[0].user_id.id, student[1], student[2], reserv)
                    student[0].delete()
                    reserv.delete()
        else:
            print(form.errors)
    else:
        form = ReservationForm()

    return redirect('profil')
    

@login_required
def directmatch(request, other_id, is_other_student, date, heure, creneau):
    
    if is_other_student == 1:
        if creneau == 1:
            reserv = Cours.objects.get(user_id=other_id, role='eleve', date1=date, heure1=heure)
        elif creneau == 2:
            reserv = Cours.objects.get(user_id=other_id, role='eleve', date2=date, heure2=heure)
        else:
            reserv = Cours.objects.get(user_id=other_id, role='eleve', date3=date, heure3=heure)

        if not reserv:
            return redirect('seances')
        student = CustomUser.objects.get(id=other_id)
        tutor = CustomUser.objects.get(id=request.user.id)
    else:
        if creneau == 1:
            reserv = Cours.objects.get(user_id=other_id, role='tuteur', date1=date, heure1=heure)
        elif creneau == 2:
            reserv = Cours.objects.get(user_id=other_id, role='tuteur', date2=date, heure2=heure)
        else:
            reserv = Cours.objects.get(user_id=other_id, role='tuteur', date3=date, heure3=heure)

        if not reserv:
            return redirect('seances')
        tutor = CustomUser.objects.get(id=other_id)
        student = CustomUser.objects.get(id=request.user.id)

    with open('hist.txt', 'a') as f:
        f.write(f"{tutor.username} {tutor.first_name} {student.username} {student.first_name} {reserv.nom_matiere} {date} {heure}\n")

    send_email_match(tutor.id, student.id, date, heure, reserv)
    reserv.delete()

    return redirect('seances')


@login_required
def seances(request):
    eleves = Cours.objects.filter(role='eleve')
    tuteurs = Cours.objects.filter(role='tuteur')

    eleves = eleves.exclude(user_id=request.user)
    tuteurs = tuteurs.exclude(user_id=request.user)

    return render(request, 'seances.html', {'eleves': eleves, 'tuteurs': tuteurs})


@login_required
def profil(request):
    with open('hist.txt', 'r') as f:
        history = f.readlines()

    history = [line.split(" ") for line in history if str(request.user.username) in line]
    
    mounths = {
        1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin',
        7: 'Juillet', 8: 'Août', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
    }

    for line in history:
        day = line[5][8:]
        mounth = line[5][5] + line[5][6]
        mounth = mounths[int(mounth)]
        year = line[5][:4]

        line[5] = f"{day} {mounth} {year}"

    history.reverse()

    eleves = Cours.objects.filter(user_id=request.user, role='eleve')
    tuteurs = Cours.objects.filter(user_id=request.user, role='tuteur')

    return render(request, 'profil.html', {'history': history, 'eleves': eleves, 'tuteurs': tuteurs})


@login_required
def calendrier(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()

    return render(request, 'calendrier.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')