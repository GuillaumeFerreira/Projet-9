[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Projet-9 Développez une application Web en utilisant Django
## Description
Application web utilisant le framework Django
## Fonctionnalités
* S'incrire, se connecter, s'abonner
* Demander ou publier des critiques de livres ou d’articles
##### Télécharger le projet 
``` 
git clone https://github.com/GuillaumeFerreira/Projet-9.git
```
ou
> https://github.com/GuillaumeFerreira/Projet-9/archive/refs/heads/main.zip
##### Créer l'environnement virtuel
```python 
python -m venv env
```
##### Activer l'environnement virtuel
```python 
env\Scripts\activate.bat
```
#### Installer les librairies necessaires
```python 
pip install -r Litreview\requirements.txt
```
#### Configuration base de données
```python 
python Litreview\manage.py makemigrations
```
```python 
python Litreview\manage.py migrate
```
#### Lancer le serveur
```python
python Litreview\manage.py runserver
```
#### Visualiser l'application sur un navigateur
> http://127.0.0.1:8000/
## Contribuer
Pour toutes contibutions, veuillez utiliser **flake8** et **black**
#### Exécuter black
```python
black Litreview
```
#### Exécuter flake8
```python
flake8 Litreview
```