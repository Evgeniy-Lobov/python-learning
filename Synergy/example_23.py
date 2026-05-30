import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # Засекаем время начала выполнения
        result = func(*args, **kwargs) # Вызываем оригинальную функцию
        end_time = time.time() # Засекаем время окончания выполнения
        print(f"Время выполнения {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


# Тестируем
@time_decorator
def slow_function():
    time.sleep(0.1)
    return "Завершено"


@time_decorator
def fast_function():
    sum(range(1000))
    return "Быстро"


slow_function()  # Вывод будет
fast_function()  # Вывод будет, даже если операция быстрая


@time_decorator
def example_function():
    for _ in range(1000000):
        pass #Простая операция для имитации работы функции

example_function() #Время выполнения example_function:0.05секунд