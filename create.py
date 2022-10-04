import json


def gen_person():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    tel = input('Введите номер телефона:')
    description = input('Дополнительная информация:')

    person = {
        'id':0,
        'surname': surname,
        'name': name,
        'tel': tel,
        'description': description
    }
    return person


def write_json(person_dict):
    try:
        with open('phone_directory.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = []

    person_dict['id'] = len(data)
    data.append(person_dict)


    with open('phone_directory.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('Контакт успешно добавлен')


def main():
    for i in range(1):
        write_json(gen_person())


if __name__ == '__main__':
    main()
