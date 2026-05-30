#Пример использования абстрактных классов

# Рассмотрим пример системы, которая обрабатывает разные типы документов.
# Каждый тип документа (текстовый файл, PDF, изображение) должен иметь метод для загрузки
# содержимого и метод для отображения содержимого.
# Можно определить абстрактный класс Document, который будет содержать эти методы.

from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def load(self, filepath):
        pass

    @abstractmethod
    def display(self):
        pass

class TextDocument(Document):
    def __init__(self):
        self.content = ""

    def load(self, filepath):
        with open(filepath, 'r') as file:
            self.content = file.read()
        # Представим, что мы загружаем PDF файл
        #self.content = "Text Content"

    def display(self):
        print(f"Text Document Content:\n{self.content}")

class PDFDocument(Document):
    def __init__(self):
        self.content= ""

    def load(self, filepath):
        # Представим, что мы загружаем PDF файл
        self.content = "PDF Content"

    def display(self):
        print(f"PDF Document Content:\n{self.content}")

class ImageDocument(Document):
    def __init__(self):
        self.content = ""

    def load(self, filepath):
        # Представим, что мы загружаем изображение
        self.content = "Image Content"

    def display(self):
        print(f"Image Document Content:\n{self.content}")


# Примеры использования
text_doc = TextDocument()
text_doc.load('example.txt')
text_doc.display()

pdf_doc = PDFDocument()
pdf_doc.load('example.pdf')
pdf_doc.display()

image_doc = ImageDocument()
image_doc.load('example.jpg')
image_doc.display()