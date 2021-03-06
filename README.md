[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Développez une application Web en utilisant Django
## Description
Application web utilisant le framework Django
## Fonctionnalités
* S'incrire, se connecter, s'abonner
* Demander ou publier des critiques de livres ou d’articles
## Instructions détaillant la configuration
##### Télécharger le projet 
``` 
git clone https://github.com/GuillaumeFerreira/Projet-9.git
```
ou
> https://github.com/GuillaumeFerreira/Projet-9/archive/refs/heads/main.zip
##### Créer l'environnement virtuel
```
python -m venv env
```
##### Activer l'environnement virtuel
``` 
env\Scripts\activate.bat
```
#### Installer les librairies necessaires
```
pip install -r Litreview\requirements.txt
```
#### Lancer le serveur
```
python Litreview\manage.py runserver
```
#### Visualiser l'application sur votre navigateur
> http://127.0.0.1:8000/
## Tester l'application via l'interface web
En utilisant la base de données fourni dans le projet, vous pouvez vous identifier avec 2 comptes:
#### Identifiants:
```
compte-1
```
```
compte-2
```
#### Mot de passe:
Le mot de passe est identique pour les deux comptes
```
Guillaume46@
```
### Panel administration
Vous pouvez accéder au panel d'administration de django avec le lien et l'identifiant suivant:
#### Lien:
> http://127.0.0.1:8000/admin
#### Identifiant:
```
ferreira
```
#### Mot de passe:
```
Guillaume46@
```
## Contribuer
Pour toutes contibutions, veuillez utiliser **black** et **flake8**
#### Exécuter black
```
black Litreview
```
#### Exécuter flake8
```
flake8 Litreview
```