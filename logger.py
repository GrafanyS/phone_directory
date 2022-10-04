# импорт необходимых библиотек
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime as dt
from db_link import *
import time
import logging
import sys

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
        

start = time.perf_counter()
change_con(LOG)
import_csv(LOG)
finish = time.perf_counter()
print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")

FORMATTER = logging.Formatter("%(time)s — %(name)s — %(level)s — %(message)s")
LOG_FILE = LOG

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # лучше иметь больше логов, чем их нехватку
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


get_logger(LOG)
