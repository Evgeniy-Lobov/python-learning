# Глобальная переменная для хранения общего количества транзакций
total_transactions = 0

def transaction_manager():
    # Локальная переменная для хранения транзакций в текущей сессии
    session_transactions = 0

    def start_transaction():
        nonlocal session_transactions
        session_transactions += 1
        print(f"Transaction {session_transactions} started in this session.")

    def commit_transaction():
        nonlocal session_transactions
        global total_transactions
        total_transactions += 1
        print(f"Transaction {session_transactions} committed. Total transactions: {total_transactions}")

    def rollback_transaction():
        nonlocal session_transactions
        print(f"Transaction {session_transactions} rolled back.")
        session_transactions -= 1

    def end_session():
        print(f"Session ended with {session_transactions} transactions.")

    #Симуляция транзакций в сессии
    start_transaction()
    commit_transaction()
    start_transaction()
    rollback_transaction()
    start_transaction()
    commit_transaction()
    end_session()

#Запуск нескольких сессий транзакций
print("Starting Session1")
transaction_manager()

print("\nStartingSession2")
transaction_manager()

print("\nTotal transactions processed:", total_transactions)