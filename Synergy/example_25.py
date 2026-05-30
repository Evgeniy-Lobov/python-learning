# Пример:Класс "Книга"
# Рассмотрим класс "Книга", который содержит информацию о книгах в библиотеке.
# Этот пример демонстрирует создание экземпляров класса и использование их атрибутов.

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title                  # Название книги
        self.author = author                # Автор книги
        self.year = year                    # Год издания
        self.genre = genre                  # Жанр книги
        self.checked_out = False            # Статус наличия книги (на руках или в библиотеке)

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f'Книга "{self.title}" взята на руки.'
        else:
            return f'Книга "{self.title}" уже взята.'

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return f'Книга "{self.title}" возвращена в библиотеку.'
        else:
            return f'Книга "{self.title}" уже находится в библиотеке.&apos'

    def book_info(self):
        status = 'на руках' if self.checked_out else 'в библиотеке'
        return (f'Название: {self.title}\n'
                f'Автор: {self.author}\n'
                f'Год издания: {self.year}\n'
                f'Жанр: {self.genre}\n'
                f'Статус: {status}')

    def __del__(self):
        print(f'Книга "{self.title}" удалена из памяти.')

#Создание экземпляров класса
# Создание нескольких экземпляров класса Book
book1 = Book("1984", "Джордж Оруэлл", 1949, "Дистопия")
book2 = Book("Убить пересмешника", "Харпер Ли", 1960, "Драма")
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика")

# Создание списка для хранения экземпляров книг
library = [book1, book2, book3]

# Вывод информации о каждой книге в библиотеке

for book in library:
    print(book.book_info())
    print()                                 # Пустая строка для разделения информации

# Взятие книги на руки
print(book1.check_out())
print()

# Попытка взять ту же книгу снова
print(book1.check_out())
print()

# Возврат книги в библиотеку
print(book1.return_book())
print()

# Снова вывод информации о книгах после изменений
for book in library:
    print(book.book_info())
    print()