# импорт необходимых библиотек
import json
import csv
from colorama import Fore, Back, Style
from db_link import *
import logger


def export():
    try:
        num = int(input('Введите формат для экспорта (1 - .csv 2 - .json 3 - .txt): '))
        if num == 1:
            export_csv()
        elif num == 2:
            export_json()
        elif num == 3:
            export_txt()
        else:
            print('Вы ввели неверный номер')
    except:
        print('Вы ввели не число')


def export_csv():
    with open(jsonFilename, 'r', encoding='utf-8') as f:
        phone_dir = json.load(f)
    count = 0
    with open(csvFilename, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        for row in phone_dir:
            if count == 0:
                data = row.keys()
                file_writer.writerow(data)
            count += 1
            file_writer.writerow(row.values())
    logger.export_csv()
    print(Fore.GREEN + f"Экспорт завершен успешно. "
                       f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)


def export_json():
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
                    'id': row[0], 'surname': row[1], 'name': row[2], 'tel': row[3], 'description': row[4]}
                result.append(temp_dict)

            count += 1
    with open(jsonFile, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
    logger.export_json()
    print(Fore.GREEN + f'Импорт завершен успешно. '
                       f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)


def export_txt():
    with open(jsonFilename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    count = 0
    str_data = ''
    for elem in data:
        for key, val in elem.items():
            str_data += str(key) + ': ' + str(val) + '\n'
        str_data += '\n'
        count += 1
    with open(textFile, mode="w", encoding='utf-8') as file:
        file.write(str_data)
    logger.export_txt()
    print(Fore.GREEN + f"Экспорт завершен успешно. "
                       f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)

# export_csv()
# logger.export_json()
# export_txt()
