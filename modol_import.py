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
# def conv_json(csvFilename, jsonFilename):
#     # создание списков
#     data = []
#
#     # считывание данных из CSV-файла
#     with open(csvFilename, 'r', encoding='utf-8') as csvfile:
#         csvRead = csv.DictReader(csvfile)
#
#         # Преобразование строк в списке и добавление его к данным
#         for rows in csvRead:
#             data.append(rows)
#
#     # сброс данных
#     with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
#         jsonString = json.dumps(data, indent=4)
#         jsonfile.write(jsonString)
#
#
# # имена файлов
# csvFilename = r'phone_directory.csv'
# jsonFilename = r'phone_directory.json'
# csvFile = r'phone_directory_export.csv'
# jsonFile = r'phone_directory_export.json'
#
# start = time.perf_counter()
# # Вызов функции преобразования
# conv_json(csvFilename, jsonFilename)
# finish = time.perf_counter()
# print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")
#
# with open(jsonFile, 'r') as jsonfile:
#     data = jsonfile.read()
#     jsonobj = json.loads(data)
#
#
# def convcsv(input_json, output_path):
#     keylist = []
#     for key in jsonobj[0]:
#         keylist.append(key)
#     f = csv.writer(open(output_path, "w"))
#     f.writerow(keylist)
#
#     for record in jsonobj:
#         currentrecord = []
#     for key in keylist:
#         currentrecord.append(record[key])
#         f.writerow(currentrecord)
#
#
# start = time.perf_counter()
# convcsv(jsonobj, csvFile)
# finish = time.perf_counter()
# print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")


def import_csv():
    result = []
    with open("file_for_import.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue

            else:
                temp_dict = {'surname': row[0], 'name': row[1], 'tel': row[2], 'comment': row[3]}
                result.append(temp_dict)

            count += 1
    with open('data_base.json', 'w') as file:
        json.dump(result, file, indent=2)

    print(f'\033[30m\033[42m\033[4m Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов. \033[0m')
