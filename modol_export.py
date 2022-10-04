import json
import csv
import logger


def export():
    with open('phone_directory.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    count = 0
    with open("phone_directory_export.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Телефон", "Описание"])
        for i in data:
            file_writer.writerow([i["id"], i["surname"],i["name"], i["tel"], i["description"]])
            count+=1
    logger.export_csv()
    print(f'Экспорт завершен успешно.')
    print(f'Всего экспортировано {count} контактов.')

