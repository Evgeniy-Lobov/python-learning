# Пример с классом Vector

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Примеры использования
v1 = Vector(2,3)
v2 = Vector(4,5)

# Сложение
v3 = v1 + v2
print(v3)                                     # Output:Vector(6,8)

# Вычитание
v4 = v1 - v2
print(v4)                                     # Output:Vector(-2,-2)

# Умножение на скаляр
v5 = v1 * 3
print(v5)                                     # Output:Vector(6,9)

# Деление на скаляр
v6 = v2 / 2
print(v6)                                     # Output:Vector(2.0,2.5)

# #Сравнение
print(v1 == v2)                               # Output:False
print(v1 == Vector(2,3))                # Output:True