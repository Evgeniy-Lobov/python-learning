# Рассмотрим практический пример, в котором создается декоратор класса
# для добавления логирования ко всем методам класса.
#
# Допустим, есть система управления банковскими счетами, и нам нужно логировать
# все операции, такие как депозиты и снятие средств.

def log_methods(cls):
    """
    Декоратор класса, который добавляет логирование ко всем методам класса.
    """

    class WrappedClass:
        def __init__(self,*args,**kwargs):
            self._wrapped= cls(*args,**kwargs)

        def __getattr__(self,name):
            attr = getattr(self._wrapped, name)
            if callable(attr):
                def logged(*args, **kwargs):
                    print(f"Calling method {name} with arguments {args} and{kwargs}")
                    result = attr(*args, **kwargs)
                    print(f"Method {name} returned {result}")
                    return result
                return logged
            return attr
    return WrappedClass

@log_methods
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

#Примеры использования
account = BankAccount("Alice",100)
print(account.deposit(50))              # Добавляет 50 к балансу
print(account.withdraw(30))             # Снимает 30 с баланса
print(account.get_balance())            # Получает текущий баланс