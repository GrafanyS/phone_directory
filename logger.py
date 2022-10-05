# импорт необходимых библиотек
import logging
from datetime import datetime as dt
from db_link import *


# import time

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


def export_csv(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Export all contact in .csv;\n')


def import_csv(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Import all contact from .csv;\n')


def change_con(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Contact change;new contact;\n')


logger = logging.getLogger(__name__)

# def info_logger():
#     logger = logging.getLogger(LOG)
#     logger.setLevel(logging.DEBUG)
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     logger.debug('debug message')
#     logger.info('info message')
#     logger.warning('warn message')
#     logger.error('error message')
#     logger.critical('critical message')


# start = time.perf_counter()
# change_con(LOG)
# import_csv(LOG)
# finish = time.perf_counter()
# print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")
# info_logger()
