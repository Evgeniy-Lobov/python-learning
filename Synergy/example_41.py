# Пример кода для проверки существования базы данных и подключения к ней:

import os
import sqlite3

def main():
    db_name = 'my_todo_list.db'
    db_is_new = not os.path.exists(db_name)

    connection = sqlite3.connect(db_name)

    if db_is_new:
        print('Создание новой базы данных! Объявите структуру схемы данных!')
    else:
        print('Подключение к уже существующей базе данных!')


if __name__ == "__main__":
    main()