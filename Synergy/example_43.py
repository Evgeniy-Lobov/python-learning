import sqlite3


def fetch_data_as_is(db_name):
    # Подключение к базе данных
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Выполнение запроса для получения всех задач
    cursor.execute('SELECT id, priority, description, status, deadline, completed, project FROM tasks')

    # Извлечение данных в виде кортежей
    rows = cursor.fetchall()

    for row in rows:
        print(type(row))
        print(row)

    # Закрытие соединения
    connection.close()

if __name__ == "__main__":
    fetch_data_as_is('projects_and_tasks.db')
