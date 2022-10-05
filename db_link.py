from sys import platform


if platform == "linux" or platform == "linux2":
    csvFilename = r'DB_Directory/phone_directory.csv'
    jsonFilename = r'DB_Directory/phone_directory.json'
    csvFile = r'DB_export/phone_directory_export.csv'
    jsonFile = r'DB_export/phone_directory_export.json'
    LOG = r'Logger/logger.log'
elif platform == "darwin":
    csvFilename = r'DB_Directory/phone_directory.csv'
    jsonFilename = r'DB_Directory/phone_directory.json'
    csvFile = r'DB_export/phone_directory_export.csv'
    jsonFile = r'DB_export/phone_directory_export.json'
    LOG = r'Logger/logger.log'
elif platform == "win32":
    csvFilename = r'DB_Directory\phone_directory.csv'
    jsonFilename = r'DB_Directory\phone_directory.json'
    csvFile = r'DB_export\phone_directory_export.csv'
    jsonFile = r'DB_export\phone_directory_export.json'
    LOG = r'Logger\logger.log'
