# импорт необходимых библиотек
import os
import csv 
import json
import time
# import pandas as pd

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]


# with open('phone_directory.csv', 'a', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for row in data:
#         writer.writerow(row)

# with open('phone_directory.csv') as f:
#     print(f.read())

# определение функции для преобразования файла CSV в файл JSON
def convjson(csvFilename, jsonFilename): 
     
    # создание списков
    data = [] 
     
    # считывание данных из CSV-файла
    with open(csvFilename, 'r', encoding = 'utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile) 
         
        # Преобразование строк в списка и добавление его к данным
        for rows in csvRead:
            data.append(rows)
 
    # сброс данных
    with open(jsonFilename, 'w', encoding = 'utf-8') as jsonfile: 
        jsonString = json.dumps(data, indent=4)
        jsonfile.write(jsonString)

  

# имена файлов
csvFilename = r'phone_directory.csv'
jsonFilename = r'phone_directory.json'
csvFile = r'phone_directory1.csv'
jsonFile = r'phone_directory1.json'


start = time.perf_counter()
# Вызов функции преобразования
convjson(csvFilename, jsonFilename)
finish = time.perf_counter()
print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")


with open(jsonFile, 'r') as jsonfile:
    data = jsonfile.read()
    jsonobj = json.loads(data)


def convcsv(input_json, output_path):
    keylist = []
    for key in jsonobj[0]:
        keylist.append(key)
    f = csv.writer(open(output_path, "w"))
    f.writerow(keylist)

    for record in jsonobj:
        currentrecord = []
    for key in keylist:
      currentrecord.append(record[key])
      f.writerow(currentrecord)


start = time.perf_counter()
convcsv(jsonobj, csvFile)
finish = time.perf_counter()
print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")

