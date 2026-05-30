def log_file_reader(file_path, keyword):
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                yield line

# Пример содержимого файла example.log
log_content = """
INFO: User logged in
ERROR: Unable to connect to database
INFO: Data processed successfully
ERROR: Timeout occurred
"""

# Запись содержимого в файл для демонстрации
with open('example.log', 'w') as log_file:
    log_file.write(log_content)

# Использование генератора для поиска строк с ключевым словом "ERROR"
for line in log_file_reader('example.log', 'ERROR'):
    print(line, end='')

