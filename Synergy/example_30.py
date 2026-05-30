# Есть библиотека, в которой есть книги и читатели.
# Книга имеет название, автора и статус(доступна или выдана).
# Читатель может взять книгу и вернуть её.
# Библиотека управляет списком книг и списком читателей.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status='available' if self.is_available else 'checked out'
        return f'"{self.title}" by {self.author}({status})'

class Reader:
    def __init__(self, name):
        self.name= name
        self.borrowed_books= []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed {book}')
        else:
            print(f'{book} is not available')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f'{self.name} returned {book}')
        else:
            print(f'{self.name} does not have {book}')

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def create_book(self,title,author):
        book = Book(title, author)
        self.add_book(book)
        print(f'Created and added {book} to the library')

    def create_reader(self,name):
        reader = Reader(name)
        self.add_reader(reader)
        print(f'Created and added reader {reader.name}')

    def add_book(self,book):
        self.books.append(book)
        print(f'Added {book} to the library')

    def add_reader(self,reader):
        self.readers.append(reader)
        print(f'Added reader {reader.name}')

    def display_books(self):
        for book in self.books:
            print(book)

# Использование композиции
library=Library()

# Создаем и добавляем книги в библиотеку
library.create_book("1984","GeorgeOrwell")
library.create_book("АннаКаренина","ЛевТолстой")

# Создаем и добавляем читателя
library.create_reader("Alice")

# Получаем первого читателя и первую книгу для примера
reader = library.readers[0]
book = library.books[0]

# Читатель берет книгу
reader.borrow_book(book)

# Попытка взять книгу, которая уже взята
reader.borrow_book(book)

# Возвращение книги
reader.return_book(book)

#Показать все книги в библиотеке
library.display_books()