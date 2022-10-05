# импорт необходимых библиотек
import json
import csv
from colorama import Fore, Back, Style
from db_link import *


def export_csv():
    with open(jsonFile, 'r', encoding='utf-8') as f:
        phone_dir = json.load(f)
    count = 0
    with open(csvFile, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        for row in phone_dir:
            if count == 0:
                data = row.keys()
                file_writer.writerow(data)
            count += 1
            file_writer.writerow(row.values())
    print(Fore.BLACK + Back.GREEN + f"Экспорт завершен успешно. "
                                         f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)


# export_csv()
