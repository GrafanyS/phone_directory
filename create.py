import json


def gen_person():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    tel = input('Введите номер телефона:')
    description = input('Дополнительная информация:')

    person = {
        'surname': surname,
        'name': name,
        'tel': tel,
        'description': description
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('DB_Directory/phone_directory.json'))
    except:
        data = []

    data.append(person_dict)

    with open('DB_Directory/phone_directory.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    for i in range(1):
        write_json(gen_person())


if __name__ == '__main__':
    main()
