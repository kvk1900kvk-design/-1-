class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнення: +{amount}. Новий баланс: {self.balance}")
        else:
            print("Сума поповнення має бути більшою за 0!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття має бути більшою за 0!")
        elif amount > self.balance:
            print("Недостатньо коштів!")
        else:
            self.balance -= amount
            print(f"Зняття: -{amount}. Новий баланс: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account
        print(f"Рахунок {account.account_number} успішно додано")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Рахунок не знайдено!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Рахунок не знайдено!")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            print("Один із рахунків не знайдено!")
            return

        if amount <= 0:
            print("Сума переказу має бути більшою за 0!")
            return

        if self.accounts[from_acc].balance < amount:
            print("Недостатньо коштів для переказу!")
            return

        self.accounts[from_acc].withdraw(amount)
        self.accounts[to_acc].deposit(amount)
        print(f"Переказ {amount} від {from_acc} до {to_acc} виконано")

bank = Bank()

acc1 = BankAccount("Іван Петренко", "12345", 500)
acc2 = BankAccount("Марія Іванова", "67890", 1000)

bank.add_account(acc1)
bank.add_account(acc2)

bank.deposit("12345", 300)
bank.withdraw("67890", 200)
bank.transfer("12345", "67890", 400)
