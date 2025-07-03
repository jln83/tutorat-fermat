# Tutorat Fermat

---

## Fonctionnalités

- Authentification élèves/tuteurs (Django Auth)
- Création/recherche d’annonces de tutorat
- Annonces par mail de 
- Administration via Django Admin

---

##  Architecture du projet

À la racine, on trouve le fichier `manage.py`, qui est l'utilitaire principal pour interagir avec Django (lancement du serveur, migrations, création d'utilisateurs...).

Le répertoire `tutorat/` contient les fichiers de configuration du projet Django : les paramètres (`settings.py`), la gestion des routes globales (`urls.py`), ainsi que les points d'entrée ASGI et WSGI pour le déploiement.

L'application principale s'appelle `core/`. Elle regroupe toute la logique de l'application :
- `models.py` définit les structures de données (profils, créneaux, affectations...),
- `views.py` contient les fonctions qui gèrent les requêtes utilisateurs,
- `forms.py` regroupe les formulaires liés aux modèles ou personnalisés,
- `templates/core/` contient les pages HTML structurées avec Django Template Language,
- `urls.py` déclare les routes spécifiques à l'application.

Les fichiers statiques (images, CSS, JavaScript) sont placés dans le dossier `static/`.

Enfin, le fichier `requirements.txt` liste les dépendances Python nécessaires pour faire tourner le projet.

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/jln83/tutorat-fermat.git
cd tutorat-fermat
```

### 2. Installer les dépendances 

pip install -r requirements.txt

---

Accès :

Application : http://127.0.0.1:8000/

Admin : http://127.0.0.1:8000/admin/

--- 

Utilisation:

Connexion : via la page /connexion/

Accueil : page d’entrée dynamique selon l’utilisateur

Calendrier : permet de consulter les créneaux

Affectation : système de mise en relation entre tuteurs et élèves

Déconnexion : accessible depuis toutes les pages connectées

Les templates se trouvent dans core/templates/core/
Les routes principales sont définies dans core/urls.py.

## Contribuer


1. Fork du repo

2. Crée une branche : git checkout -b ma-feature

3. Fait tes modifications

4. Commit avec un message clair

5. Push et ouvre une Pull Request
