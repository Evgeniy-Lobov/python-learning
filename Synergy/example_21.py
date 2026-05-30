# Пример с использованием встроенных итераторов
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

print(next(iterator)) #Выводит 1
print(next(iterator)) #Выводит 2
print(next(iterator)) #Выводит 3

# Продолжение итерации
for item in iterator:
    print(item) #Выводит оставшиеся элементы 4 и 5