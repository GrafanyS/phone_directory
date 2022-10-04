# импорт необходимых библиотек
import os
import csv
import json
from db_link import *
from colorama import Fore, Back, Style
import time
import pandas as pd

def import_csv():
    result = []
    with open(csvFilename, encoding='utf-8') as r_file:
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
    with open(jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2)

    print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)


def import_json():
    result = []
    with open(csvFilename, "r", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue

            else:
                temp_dict = {
                    'surname': row[0], 'name': row[1], 'tel': row[2], 'comment': row[3]}
                result.append(temp_dict)

            count += 1
    with open(jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2)

    print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)








def convcsv():
    with open(jsonFilename, 'r', encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)

    df.to_csv(csvFile, encoding='utf-8', index=False)

start = time.perf_counter()
convcsv()
finish = time.perf_counter()
print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
      f'Всего импортировано {finish - start:0.4f} контактов.' + Style.RESET_ALL)
