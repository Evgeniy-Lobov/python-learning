try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print ("Результат:", result)
except ZeroDivisionError as e:
    print("Ошибка:Деление на ноль невозможно.")
finally:
    print("Операция завершена.")