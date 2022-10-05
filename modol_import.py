# импорт необходимых библиотек
import csv, json
from db_link import *
from colorama import Fore, Back, Style


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
    with open(jsonFile, 'w', encoding='utf-8') as file:
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
                    'id': row[0], 'surname': row[1], 'name': row[2], 'tel': row[3], 'comment': row[4]}
                result.append(temp_dict)

            count += 1
    with open(jsonFile, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)

    print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)


# import_csv()
# import_json()
