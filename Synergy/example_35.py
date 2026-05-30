# Следующий код иллюстрирует создание простого диалога типа "Введите ваше имя"

import tkinter as tk
import tkinter.simpledialog as simpledialog

# Функция для отображения диалогового окна ввода
def display_dialog():
    # Отображение диалогового окна для ввода строки
    answer = simpledialog.askstring("NameEntry","Please enter your name:")

    #Проверка, введено ли значение, и вывод результата
    if answer:
        print("Your name is:",answer)
    else:
        print("No input provided.")

# Создание главного окна
root = tk.Tk()

# Создание кнопки для отображения диалогового окна
button = tk.Button (root, text="OpenDialog", command=display_dialog)
button.pack()

# Запуск основного цикла обработки событий
root.mainloop()