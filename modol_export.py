import json
import csv


def export():
    with open('data_base.json', 'r') as f:
        phone_dir = json.load(f)
    count = 0
    with open("phone_directory_export.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Фамилия\t", "Имя\t", "Телефон\t", "Описание\t"])
        for i in phone_dir:
            file_writer.writerow([i['surname'],i['name'], i['tel'], i['comment']])
            count+=1
    print(f'\033[30m\033[42m\033[4m Экспорт завершен успешно. '
          f'Всего экспортировано {count} контактов. \033[0m')



