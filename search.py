import json
from colorama import Fore, Back, Style



def read_json(file):
    try:
         with open('phone_directory.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        print('В базе еще нет ни одного контакта :(')

def search_contact(data):
    name = input('Введите имя контакта, номер телефона или комментарий: ')
    found_contacts = []
    temp = {1:"surname", 2:"name", 3:"tel", 4:"description"}
    for index, contact in enumerate(data):
        if name.lower() in contact["surname"].lower() or name.lower() in contact["name"].lower() or name.lower() in contact["tel"].lower() or name.lower() in contact["description"].lower():
            found_contacts.append(contact)    
            print(f'Найден контакт: {contact["id"]} {contact["surname"]} {contact["name"]} {contact["tel"]} {contact["description"]}')    #Выводим заданный контакт      
    if found_contacts != []: return found_contacts
    else: 
        # print(found_contacts)
        return 'Такого контакта нет в базе.'
# data = read_json('phone_directory.json')
# search_contact(data)

