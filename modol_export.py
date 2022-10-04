# импорт необходимых библиотек
import json
import csv
from colorama import Fore, Back, Style
from db_link import *


def export():
    with open(jsonFilename, 'r', encoding='utf-8') as f:
        phone_dir = json.load(f)
    count = 0
    with open(csvFile, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Фамилия\t", "Имя\t", "Телефон\t", "Описание\t"])
        for i in phone_dir:
            file_writer.writerow([i['id']],[i['surname'], i['name'], i['tel'], i['comment']])
            count += 1
    print(Fore.BLACK + "" + Back.GREEN + f"Экспорт завершен успешно. "
                                         f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)


export()
