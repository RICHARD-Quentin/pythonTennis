# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import schedule
from controllers.data import job

# lance la fonction job tt les jours a 12h
schedule.every().days.at("12:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
# Press the green button in the gutter to run the script.


# if __name__ == '__main__':
#     from datetime import datetime
#
#     cities = [
#         'paris',
#         'tokyo',
#         'washington',
#         'lagos',
#         'canberra',
#         'moscou',
#         'wuhan',
#         'khartoum',
#         'lima',
#         'oulu'
#     ]
#
#     # 10 villes, 1 fichier json/ville, 1*/j
#
#     parsedResult = []
#     for city in cities:
#         url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a383caccdb0d3696ce5b26460b5dc3e8&units=metric'
#         r = requests.get(url)
#         result = json.loads(r.text)
#
#         logs = []
#         fileName = 'C:\\Users\\Quentin\\Documents\\Projects\\CanIRun\\data\\' + city + '-data.json'
#
#         # Check if file exists
#         if path.isfile(fileName) is False:
#             raise Exception("File not found")
#
#         with open(fileName) as outfile:
#             logs = json.load(outfile)
#
#         logs.append(result)
#         with open(fileName, 'w+') as outfile:
#             json.dump(logs, outfile, default=str)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
