import sqlite3

# Функция для чтения всех проектов из базы данных с использованием Row для доступа по именам столбцов
def read_projects(connection):
    connection.row_factory = sqlite3.Row  # Устанавливаем row_factory в Row для доступа по именам столбцов
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM projects')
        projects = cursor.fetchall()
        print("Проекты:")
        for project in projects:
            # Доступ к данным по именам столбцов
            print(f"Имя: {project['name']}, Описание: {project['description']}, Срок завершения: {project['deadline']}")
    except sqlite3.Error as e:
        print(f"Ошибка при чтении проектов: {e}")

# Функция для чтения всех задач из базы данных с использованием Row для доступа по именам столбцов
def read_tasks(connection):
    connection.row_factory = sqlite3.Row  # Устанавливаем row_factory в Row для доступа по именам столбцов
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        print("Задачи:")
        for task in tasks:
            # Доступ к данным по именам столбцов
            print(f"ID: {task['id']}, Приоритет: {task['priority']}, Описание: {task['description']}, Статус: {task['status']}, "
                  f"Срок выполнения: {task['deadline']}, Завершение: {task['completed']}, Проект: {task['project']}")
    except sqlite3.Error as e:
        print(f"Ошибка при чтении задач: {e}")

def main():
    db_name = 'projects_and_tasks.db'
    # Подключение к базе данных
    connection = sqlite3.connect(db_name)
    # Чтение данных из таблиц
    read_projects(connection)
    read_tasks(connection)
    # Закрытие соединения с базой данных
    connection.close()

if __name__ == "__main__":
    main()
