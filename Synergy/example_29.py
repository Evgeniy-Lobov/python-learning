# Определение базового класса
class Shape:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

#Создание подклассов

class Square(Shape):
    def __init__(self, side_length, x=0, y=0):
        super().__init__(x, y)                          #Вызов конструктора базового класса
        self.side_length = side_length

    def __str__(self):
        return super().__str__() + f', side_length: {self.side_length}'

class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)                          #Вызов конструктора базового класса
        self.radius = radius

    def __str__(self):
        return super().__str__() + f',radius:{self.radius}'

# Пример использования:
#Создаем экземпляры классов
square = Square(side_length=5,x=25,y=40)
circle = Circle(radius=10,x=10,y=5)

# Вывод начального состояния
print(square)       #x:25, y:40, side_length:5
print(circle)       #x:10, y:5, radius:10

# Двигаем фигуры
square.move(dx=35, dy=50)
circle.move(dx=10, dy=19)

# Вывод состояния после перемещения
print(square)       #x:60,  y:90,   side_length:5
print(circle)       #x:20, y:24, radius:10