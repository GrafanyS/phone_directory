# импорт необходимых библиотек
import csv 
import json 
 
# определение функции для преобразования файла CSV в файл JSON
def convjson(csvFilename, jsonFilename): 
     
    # создание словаря
    mydata = {} 
     
    # считывание данных из CSV-файла
    with open(csvFilename, encoding = 'utf-8') as csvfile: 
        csvRead = csv.DictReader(csvfile) 
         
        # Преобразование строк в словарь и добавление его к данным
        for rows in csvRead: 
             
            mykey = rows['S. No.'] 
            mydata[mykey] = rows 
 
    # сброс данных
    with open(jsonFilename, 'w', encoding = 'utf-8') as jsonfile: 
        jsonfile.write(json.dumps(mydata, indent = 4)) 
 

# имена файлов
csvFilename = r'phone_directory.csv'
jsonFilename = r'phone_directory.json'
 
# Вызов функции преобразования
convjson(csvFilename, jsonFilename) 
