from datetime import datetime
from os import path

import requests
import json
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def store(data, city):
    logs = []
    fileName = 'C:\\Users\\Quentin\\Documents\\Projects\\CanIRun\\data\\' + city + '-data.json'

    # Check if file exists
    if path.isfile(fileName) is False:
        raise Exception("File not found")

    with open(fileName) as outfile:
        logs = json.loads(outfile)


    logs.append(data)
    print(logs)

    #
    # with open(fileName, 'w+') as outfile:
    #     json.dump(logs, outfile, default=str)
