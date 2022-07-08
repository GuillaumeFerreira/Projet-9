[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Projet-9 Développez une application Web en utilisant Django
## Description
Application web utilisant le framework Django
## Fonctionnalités
* S'incrire, se connecter, s'abonner
* Demander ou publier des critiques de livres ou d’articles
##### créer l'environnement virtuel
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
#### Lancer le serveur
```python
python manage.py runserver
```
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