# Пример:Управление зоопарком

# Представим класс Animal, который представляет животное в зоопарке.
# Добавим переменную класса total_animals для отслеживания общего количества животных в зоопарке.

class Animal:
    total_animals = 0                           # Переменная класса
    def __init__(self, species, name):
        self.species = species                  # Переменная экземпляра
        self.name = name                        # Переменная экземпляра
        Animal.total_animals += 1               # Увеличиваем счетчик при создании экземпляра

    def __del__(self):
        Animal.total_animals -= 1               # Уменьшаем счетчик при удалении экземпляра

    def animal_info(self):
        return f'{self.species} по имени {self.name}'

    def get_total_animals(self):return f'Общее количество животных в зоопарке: {self.__class__.total_animals}'


# Создание нескольких экземпляров класса Animal
animal1 = Animal("Лев", "Симба")
animal2 = Animal("Слон", "Дамбо")
animal3 = Animal("Зебра", "Марти")

# Вывод информации о каждом животном и общем количестве животных

print(animal1.animal_info())
print(animal2.animal_info())
print(animal3.animal_info())

# Вывод общего количества животных через метод экземпляра
print(animal1.get_total_animals())

# Удаление одного из животных
del animal2

# Вывод общего количества животных через атрибут __class__
print(animal1.__class__.total_animals)
