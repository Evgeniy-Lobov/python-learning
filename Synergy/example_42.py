# В данном примере создадим две таблицы: projects для хранения проектов и tasks для
# хранения задач. В том же самом скрипте заполним созданные таблицы данными

import os
import sqlite3

# Функция для создания таблиц в базе данных
def create_tables(connection):
    cursor = connection.cursor()
    try:
        # Создание таблицы проектов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            name TEXT PRIMARY KEY,
            description TEXT,
            deadline DATE
        )
        ''')

        # Создание таблицы задач
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            priority INTEGER DEFAULT 0,
            description TEXT,
            status TEXT,
            deadline DATE,
            completed DATE,
            project TEXT NOT NULL,
            FOREIGN KEY (project) REFERENCES projects(name)
        )
        ''')

        # Сохранение изменений
        connection.commit()
        print("Таблицы успешно созданы.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблиц: {e}")
        connection.rollback()

# Функция для вставки начальных данных в таблицы
def insert_initial_data(connection):
    cursor = connection.cursor()
    try:
        # Вставка проекта "Learn Python"
        cursor.execute('''
        INSERT INTO projects (name, description, deadline)
        VALUES ('Learn Python', 'Изучить Python за 21 день', '2024-09-01')
        ''')

        # Вставка задач для проекта "Learn Python" с разными приоритетами и статусами
        cursor.execute('''
        INSERT INTO tasks (priority, description, status, deadline, completed, project)
        VALUES
        (1, 'Синтаксис и структуры данных', 'done', '2024-08-16', '2024-08-15', 'Learn Python'),
        (2, 'Функции, классы, модули', 'in progress', '2024-08-25', NULL, 'Learn Python'),
        (3, 'Работа с файлами и базами данных', 'pending', '2024-08-20', NULL, 'Learn Python'),
        (4, 'Асинхронное программирование', 'pending', '2024-08-28', NULL, 'Learn Python'),
        (5, 'Создание веб‑приложений на Flask', 'pending', '2024-09-01', NULL, 'Learn Python'),
        (2, 'Работа с библиотеками и API', 'in progress', '2024-08-22', NULL, 'Learn Python'),
        (1, 'Тестирование и отладка кода', 'pending', '2024-08-24', NULL, 'Learn Python')
        ''')

        # Сохранение изменений
        connection.commit()
        print("Начальные данные успешно вставлены.")
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")
        connection.rollback()

def main():
    db_name = 'projects_and_tasks.db'
    db_is_new = not os.path.exists(db_name)

    # Подключение к базе данных
    connection = sqlite3.connect(db_name)

    if db_is_new:
        print('Создание новой базы данных! Объявите структуру схемы данных!')
    else:
        print('Подключение к уже существующей базе данных!')

    create_tables(connection)
    insert_initial_data(connection)

    # Закрытие соединения с базой данных
    connection.close()

if __name__ == "__main__":
    main()
