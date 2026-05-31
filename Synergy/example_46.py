# Запросы с именованными параметрами используются при большом количестве параметров, а также
# при их повторении. В этом случае при формировании запроса используется обозначение
# вида `:arg_name`. Следующий пример показывает, как использовать именованные параметры для фильтрации
# задач по статусу и проекту.

import sqlite3

def fetch_tasks_by_status_and_project_named(db_name, status, project_name):
    connection = sqlite3.connect(db_name)
    # Установка row_factory для получения данных в виде словарей
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Определение запроса с именованными параметрами и явным указанием колонок
    query = '''SELECT id, priority, description, status, deadline, completed, project
              FROM tasks
              WHERE status = :status AND project = :project'''

    # Выполнение запроса с использованием именованных параметров
    cursor.execute(query, {'status': status, 'project': project_name})
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row['id']}, Priority: {row['priority']}, Description: {row['description']},"
              f"Status: {row['status']}, Deadline: {row['deadline']}, Completed: {row['completed']}, Project: {row['project']}")

    connection.close()

if __name__ == "__main__":
    fetch_tasks_by_status_and_project_named('projects_and_tasks.db', 'pending', 'LearnPython')
