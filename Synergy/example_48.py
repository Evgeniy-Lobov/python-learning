 # Для примера добавим данные о численности населения для нескольких городов.
 # Чтобы проверить, что данные были успешно добавлены, можно выполнить запрос на выборку данных из таблицы.
 # После завершения работы с базой данных закроем соединение.

import MySQLdb
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="password",
    db="world"
)
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS city (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name CHAR(35) NOT NULL,
    CountryCode CHAR(3) NOT NULL,
    District CHAR(20) NOT NULL,
    Population INT NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS city_population (
    id INT PRIMARY KEY AUTO_INCREMENT,
    city_id INT,
    year YEAR,
    population INT,
    FOREIGN KEY (city_id) REFERENCES city(ID)
);
""")
connection.commit()
print("Таблицы 'city' и 'city_population' успешно созданы.")
cursor.executemany(
    "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s);",
    [
        ("City1", "USA", "District1", 500000),
        ("City2", "USA", "District2", 1000000),
        ("City3", "USA", "District3", 1500000),
    ]
)
connection.commit()
print("Города добавлены.")
insert_data_query = """
INSERT INTO city_population (city_id, year, population)
VALUES (%s, %s, %s);
"""
population_data = [
    (1, 2020, 500000),
    (1, 2021, 505000),
    (2, 2020, 1000000),
    (2, 2021, 1005000),
    (3, 2020, 1500000),
    (3, 2021, 1510000)
]
cursor.executemany(insert_data_query, population_data)
connection.commit()
print("Данные успешно добавлены в таблицу 'city_population'.")
cursor.execute("SELECT * FROM city_population;")
rows = cursor.fetchall()
print("\nСодержимое таблицы 'city_population':")
for row in rows:
    print(row)
cursor.close()
connection.close()