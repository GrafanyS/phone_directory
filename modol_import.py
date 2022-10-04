# импорт необходимых библиотек
import os
import csv
import json
from db_link import *


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

