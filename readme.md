# Info sur ville

Simple api REST qui renvoie les informations sur la ville demander

## Installation

Installation de python 3

    sudo apt install virtualenv
    sudo apt install python3-pip
   
Création de l'environnement virtuel

    virtualenv -p python3 venv
    . venv/bin/activate
    pip install -r requirements.txt

## Démarrer

Pour Linux

    export FLASK_APP=application.py
    flask run

Pour Windows

    set FLASK_APP=application.py
    flask run
    
## Requete

La requete se fait avec un POST sous la forma d'un json.

Le json doit être sous cette forme

    {"wikipedia": Nom de la ville}
    
La réponce est la suivante

    {"summary": Text tu résumer wikipedia}
    
Example de requête en python

    responce = requests.post("http://localhost:5000",
                             data=json.dumps({"wikipedia": "paris"}),
                             headers={'Content-type': 'application/json'})
    responce.json()["summary"]
