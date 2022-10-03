import json
import csv
from colorama import Fore, Back, Style


def export():
    with open(jsonFilename, 'r', encoding='utf-8') as f:
        phone_dir = json.load(f)
    count = 0
    with open(csvFile, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Фамилия\t", "Имя\t", "Телефон\t", "Описание\t"])
        for i in phone_dir:
            file_writer.writerow([i['surname'], i['name'], i['tel'], i['comment']])
            count += 1
    print(Fore.BLACK + "" + Back.GREEN + f"Экспорт завершен успешно. "
                                         f'Всего экспортировано {count} контактов.' + Style.RESET_ALL)


csvFilename = r'DB_Directory\phone_directory.csv'
jsonFilename = r'DB_Directory\phone_directory.json'
csvFile = r'DB_export\phone_directory_export.csv'
jsonFile = r'DB_export\phone_directory_export.json'
