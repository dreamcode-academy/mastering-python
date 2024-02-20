class Account:
    def __init__(self, account_number, owner, balance = 0):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
            return
        self._balance -= amount
        print(f"{amount} withdraw. New balance: {self._balance}")

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f"Account number: {self._account_number}, Owner: {self._owner}, Balance: {self._balance}"
    

class SavingsAccount(Account):
    def apply_interest(self):
        interest = self._balance * 0.05
        self._balance += interest
        print(f"Account number: {self._account_number}, Owner: {self._owner}, Balannce: {self._balance}")

class CheckingAccount(Account):
    def issue_check(self, amount):
        self.withdraw(amount)

class Customer:
    def __init_(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
        self.__accounts = []

    def add_account(self, account):
        return self.__accounts
    
    def get_account_by_number(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
            
        return None
    
    def __str__(self):
        return f"Customer: {self.__name}, ID: {self.__id_number}"
    

class ManagerBanker:
    @staticmethod
    def audit_account(account):
        print(f"Auditing account: {account}")

    @classmethod
    def create_customer(cls, name, id_number):
        return Customer(name, id_number)
    

def get_customer(customers, id_number):
    customer = customer.get(id_number)
    

        