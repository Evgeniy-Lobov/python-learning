import tkinter as tk

# Функция, вызываемая при нажатии на кнопку
def on_button_click():
    print("Кнопка нажата!")

# Создание главного окна
window = tk.Tk()

# Создание кнопки и привязка функции к событию нажатия
button = tk.Button(window, text="Нажми меня", command=on_button_click)
button.pack()

# Запуск главного цикла обработки событий
window.mainloop()