import math_utils

def main():
    print("Сумма:", math_utils.add(10,5))
    print("Разность:", math_utils.subtract(10,5))
    print("Произведение:", math_utils.multiply(10,5))
    print("Частное:", math_utils.divide(10,5))

if __name__ == "__main__":
    main()

# Импортирование конкретных функций
from math_utils import add, divide
print(add(10,5))
print(divide(10,2))