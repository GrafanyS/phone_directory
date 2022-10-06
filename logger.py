# импорт необходимых библиотек
from concurrent.futures.thread import _worker
from datetime import datetime as dt
from db_link import *
import logging
# import time



logger = logging.getLogger(__name__)

def create_contact(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Create new contact;\n')


def delete_contact(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Delete contact;\n')
        

def export_csv():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .csv;\n')


def export_json():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .json;\n')


def export_txt():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .txt\n')


def import_txt():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .txt\n')


def import_json():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .json\n')
        

def import_csv():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .csv;\n')
        

def change_con(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Contact change;new contact;\n')


def main_logger():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=LOG,
        filemode='a',
        level=logging.DEBUG,
    )
    logger.error("Произошло что-то важное")



# start = time.perf_counter()
# change_con(LOG)
# import_csv(LOG)
# finish = time.perf_counter()
# print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")

