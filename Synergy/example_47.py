import MySQLdb

# Подключение к MySQL серверу
connection = MySQLdb.connect(
    host="localhost",  # Адрес сервера MySQL
    user="root",     # Имя пользователя MySQL
    password="password",  # Пароль пользователя
    database="world"  # Имя базы данных
)

# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Получение списка таблиц
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print("Таблицы в базе данных ‘world’:")
for table in tables:
    print(table[0])
