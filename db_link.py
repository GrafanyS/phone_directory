from distutils.text_file import TextFile
from sys import platform


if platform == "linux" or platform == "linux2":
    csvFilename = r'DB_Directory/phone_directory.csv'
    jsonFilename = r'DB_Directory/phone_directory.json'
    textFilename = r'DB_Directory/phone_directory.txt'
    csvFile = r'DB_export/phone_directory_export.csv'
    jsonFile = r'DB_export/phone_directory_export.json'
    textFile = r'DB_export/phone_directory_export.txt'
    dbFilename = r'DB_Directory/db_directory.json'
    LOG = r'Logger/logger.log'
elif platform == "darwin":
    csvFilename = r'DB_Directory/phone_directory.csv'
    jsonFilename = r'DB_Directory/phone_directory.json'
    textFilename = r'DB_Directory/phone_directory.txt'
    csvFile = r'DB_export/phone_directory_export.csv'
    jsonFile = r'DB_export/phone_directory_export.json'
    textFile = r'DB_export/phone_directory_export.txt'
    dbFilename = r'DB_Directory/db_directory.json'
    LOG = r'Logger/logger.log'
elif platform == "win32":
    csvFilename = r'DB_Directory\phone_directory.csv'
    jsonFilename = r'DB_Directory\phone_directory.json'
    textFilename = r'DB_Directory\phone_directory.txt'
    csvFile = r'DB_export\phone_directory_export.csv'
    jsonFile = r'DB_export\phone_directory_export.json'
    textFile = r'DB_export\phone_directory_export.txt'
    dbFilename = r'DB_Directory\phone_db_directory.json'
    LOG = r'Logger\logger.log'
