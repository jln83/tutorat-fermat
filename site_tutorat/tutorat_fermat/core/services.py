from django.core.mail import send_mail
from django.contrib.auth import get_user_model

#Envoie d'un mail aux deux eleves concernes par le cours (eleve, tuteur)
def send_email_match(user_id_1, user_id_2, date, heure, infos):
    
    try:

        User = get_user_model()

        # Retrieve users
        user_1 = User.objects.get(id=user_id_1)
        user_2 = User.objects.get(id=user_id_2)

        print(heure)
        print(date)

        if type(heure) != str:
            heure = heure.strftime("%H:%M")

        mois = {1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril', 5: 'mai', 6: 'juin', 7: 'juillet', 8: 'août', 9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'}

        if type(date) != str:
            date = f"{date.day} {mois[date.month]} {date.year}"
        else:
            day = date[8:]
            mounth = date[5] + date[6]
            mounth = mois[int(mounth)]
            year = date[:4]

            date_ = f"{day} {mounth} {year}"

        subject = "Un cours a été trouvé !"
        message = f"Vous avez cours de {infos.nom_matiere} le {date_} à {heure} ! Rendez vous devant le cdi à l'heure indiquée !\n\n tuteur: {user_1.first_name}\n élève: {user_2.first_name}\n\n Bon cours !\n Tutorat Fermat"

        print(user_1.email, user_2.email)
        send_mail(
            subject,
            message,
            'tutorat.lycee.fermat@gmail.com',
            [user_1.email, user_2.email]
        )
    except User.DoesNotExist:
        print("One or both users do not exist.")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")


def find_compatible_tutor(student, tutors):
    compatible_tutors = []
    for tutor in tutors:
        is_c = is_compatible(student, tutor)
        if is_c[0]:
            compatible_tutors.append(tutor)
    if not compatible_tutors: return None
    return compatible_tutors[0], is_c[1], is_c[2]


def find_compatible_student(tutor, students):
    compatible_students = []
    for student in students:
        is_c = is_compatible(student, tutor)
        if is_c[0]:
            compatible_students.append(student)
    if not compatible_students: return None
    return compatible_students[0], is_c[1], is_c[2]


def is_compatible(student, tutor):


    if not student.nom_matiere == tutor.nom_matiere:
        return False, 0, 0
    
    niveaux = {'seconde': 0, 'premiere': 1, 'terminale': 2}
    if niveaux[student.niveau] > niveaux[tutor.niveau]:
        return False, 0, 0
    
    s_dates = [[student.date1, student.heure1], [student.date2, student.heure2], [student.date3, student.heure3]]
    t_dates = [[tutor.date1, tutor.heure1], [tutor.date2, tutor.heure2], [tutor.date3, tutor.heure3]]

    for s_date in s_dates:
        for t_date in t_dates:
            if s_date == t_date:
                return True, s_date[0], s_date[1]
    
    return False, 0, 0


