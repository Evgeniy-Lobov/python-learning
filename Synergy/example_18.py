import time

# Использование встроенной функции sorted ()
start_time = time.time()
sorted_list = sorted([5, 3, 8, 1, 2, 7, 6, 4])
print("Время сортировки встроенной функцией:",time.time() - start_time)

# Пользовательская реализация сортировки (например, пузырьковый метод)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

start_time = time.time()
bubble_sorted_list = bubble_sort([5, 3, 8, 1, 2, 7, 6, 4])
print("Время сортировки пользовательской функцией:", time.time() - start_time)

