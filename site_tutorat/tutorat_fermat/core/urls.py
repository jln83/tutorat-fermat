# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('calendrier/', views.calendrier, name='calendrier'),
    path('logout/', views.logout_view, name='logout'),
    path('profil/', views.profil, name='profil'),
    path('reserver/', views.reserver, name='reserver'),
    path('creationdecompte/', views.creationdecompte, name='creationdecompte'),
    path('seances/', views.seances, name='seances'),    
    path('direct/<int:other_id>/<int:is_other_student>/<str:date>/<str:heure>/<int:creneau>', views.directmatch, name='direct'),
    path('confidentialite/', views.confidentialite, name='confidentialite'),
]