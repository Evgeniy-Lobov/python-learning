# Давайте рассмотрим практичный пример использования модуля `ttk` в Tkinter.
# Создадим приложение для управления списком задач с использованием виджетов `ttk`, таких как `Entry`,
# `Button`, `Listbox` и `Combobox`.
# Это приложение будет позволять пользователям добавлять задачи, выбирать их приоритет и просматривать
# список задач.
#
# Приложение для управления задачами. Это приложение будет содержать:
# * поле для ввода задачи;
# * комбобокс для выбора приоритета задачи (например, низкий, средний, высокий);
# * кнопку для добавления задачи в список;
# * список задач, отображающий все добавленные задачи с их приоритетом.

import tkinter as tk
from tkinter import ttk

def add_task():
    task = task_entry.get()
    priority = priority_combobox.get()

    if task:
        task_listbox.insert (tk.END, f"{task} - {priority}")
        task_entry.delete (0, tk.END)
        priority_combobox.set ("Низкий")

# Создаем главное окно приложения
root = tk.Tk()
root.title ("Менеджер задач")

# Создаем фрейм для ввода задачи и выбора приоритета
input_frame = ttk.Frame (root, padding="10")
input_frame.pack (padx=10, pady=10)

# Создаем поле для ввода задачи
task_entry=ttk.Entry (input_frame, width=30)
task_entry.grid (row=0, column=0, padx=5, pady=5)

# Создаем комбобокс для выбора приоритета
priorities = ["Низкий", "Средний", "Высокий"]
priority_combobox = ttk.Combobox(input_frame, values=priorities, state="readonly")
priority_combobox.set ("Низкий")
priority_combobox.grid (row=0, column=1, padx=5, pady=5)

# Создаем кнопку для добавления задачи
add_button = ttk.Button (input_frame, text="Добавить задачу",command=add_task)
add_button.grid (row=0, column=2, padx=5, pady=5)

# Создаем список задач
task_listbox = tk.Listbox (root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack (padx=10, pady=10)

# Запуск основного цикла приложения
root.mainloop()