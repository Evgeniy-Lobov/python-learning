# Пример использования метода класс

class Employee:
    total_employees = 0                 #Переменная класса для отслеживания общего количества сотрудников

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1       #Увеличиваем счётчик сотрудников при создании экземпляра

    def __del__(self):
        Employee.total_employees -= 1       #Уменьшаем счётчик сотрудников при удалении экземпляра


    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split('-')
        salary = float(salary)
        return cls(name, salary)

    @classmethod
    def get_total_employees(cls):
        return f'Общее количество сотрудников: {cls.total_employees}'

    def employee_info(self):
        return f'Сотрудник: {self.name}, Зарплата: {self.salary}'

# Создание экземпляров класса Employee
employee1 = Employee("Alice", 70000)
employee2 = Employee("Bob", 50000)
employee3 = Employee.from_string("Charlie-60000")

# Вывод информации о каждом сотруднике и общем количестве сотрудников
print(employee1.employee_info())
print(employee2.employee_info())
print(employee3.employee_info())
print(Employee.get_total_employees())

# Удаление одного из сотрудников

del employee1

# Общее количество сотрудников после удаления
print(Employee.get_total_employees())