# импорт необходимых библиотек
import csv, json
from db_link import *
from colorama import Fore, Back, Style
import logger


def export():
    try:
        num = int(input('Введите формат для импорта (1 - .csv или 2 - .txt): '))
        if num == 1:
            import_csv()
        elif num == 2:
            import_json()
        elif num == 3:
            import_txt()
        else:
            print('Вы ввели неверный номер')
    except:
        print('Вы ввели не число')


def import_csv():
    with open(jsonFile, 'r', encoding='utf-8') as f:
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
    logger.import_csv()

    print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)


def import_json():
    result = []
    with open(csvFile, "r", encoding='utf-8') as r_file:
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
    with open(jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)

    print(Fore.BLACK + "" + Back.GREEN + f'Импорт завершен успешно. '
          f'Всего импортировано {count - 1} контактов.' + Style.RESET_ALL)


def import_txt():
    with open(jsonFile, 'r', encoding='utf-8') as file:
        data = json.load(file)
    count = 0
    str_data = ''
    for elem in data:
        for key, val in elem.items():
            str_data += str(key) + ': ' + str(val) + '\n'
        str_data += '\n'
        count += 1
    with open(textFilename, mode="w", encoding='utf-8') as file:
        file.write(str_data)
    logger.import_txt()
    print(Fore.BLACK + Back.GREEN + f"Экспорт завершен успешно. "
          f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)


# import_csv()
# import_json()
