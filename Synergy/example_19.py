import math

def find_primes_in_range(start,end):
    """
    Находит все простые числа в заданном диапазоне.
    :param start: Начало диапазона (включительно)
    :param end: Конец диапазона (включительно)
    :return: Список простых чисел
    """
    primes = []

    def is_prime(n):
        """
        Проверяет, является ли число простым.
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) +1):
            if n % i == 0:
                return False
            return True
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

#Пример использования функции
print(f"Простые числа в диапазоне от 10 до 50: {find_primes_in_range(10,50)}")
