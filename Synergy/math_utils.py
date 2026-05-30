# math_utils.py

def add(x,y):
    """Возвращает сумму двух чисел"""
    return x + y

def subtract(x,y):
    """Возвращает разность двух чисел"""
    return x -y

def multiply(x,y):
    """Возвращает произведение двух чисел"""
    return x * y

def divide (x,y):
    """Возвращает частное двух чисел, если делитель не равен нулю"""
    if y==0:
        raise ValueError("Делитель не может быть нулем!")
    return x / y
