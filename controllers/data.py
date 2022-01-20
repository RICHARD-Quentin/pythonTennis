from os import path
import requests
import json
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def job():
    print("Job launched")

    #paramètre de l'api
    cities = [
        'paris',
        'tokyo',
        'washington',
        'lagos',
        'canberra',
        'moscou',
        'wuhan',
        'khartoum',
        'lima',
        'oulu'
    ]

    #boucle sur les params de l'api
    for city in cities:

        #construction de l'url avec la paramètre
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a383caccdb0d3696ce5b26460b5dc3e8&units=metric'
        r = requests.get(url)
        result = json.loads(r.text)

        #chemin vers le fichier
        fileName = 'C:\\Users\\Quentin\\Documents\\Projects\\CanIRun\\data\\' + city + '-data.json'

        # Check si le fichier exists
        if path.isfile(fileName) is False:
            raise Exception("File not found")

        #recupération des logs
        with open(fileName) as outfile:
            logs = json.load(outfile)

        #ajout d'une ligne de log
        logs.append(result)

        #ecriture des logs
        with open(fileName, 'w+') as outfile:
            json.dump(logs, outfile, default=str)