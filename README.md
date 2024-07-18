# Simple Django Project

Ce projet est un exemple simple d'application Django.

## Prérequis

- Python 3.x
- Pip (gestionnaire de paquets pour Python)
- Virtualenv (optionnel, mais recommandé)

## Installation

### Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/KonquerorK/django-todo-app.git
cd django-todo-app
```

### Créer un environnement virtuel

Sur macOS/Linux :

```bash
source env/bin/activate
```

Sur Windows :
```bash
.\env\Scripts\activate
```

### Configuration de la base de données

Appliquez les migrations de la base de données pour configurer votre base de données :

```bash
python manage.py migrate
```

### Créer un superutilisateur

Créez un superutilisateur pour accéder à l'interface d'administration Django :
```
python manage.py createsuperuser
```

### Démarrage du serveur de développement

Démarrez le serveur de développement Django :
```
python manage.py runserver
```



