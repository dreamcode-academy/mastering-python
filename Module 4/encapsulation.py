class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance is {self.__balance}")
        else:
            print("Invalid deposit amount")

    def wihdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance-= amount
            print(f"{amount} withdrawal. New balance is {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
account.wihdrawal(200)