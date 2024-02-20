class Account:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number  # Protected attribute
        self._owner = owner  # Protected attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")
            return
        self._balance -= amount
        print(f"{amount} withdrawn. New balance: {self._balance}")

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account Number: {self._account_number}, Owner: {self._owner}, Balance: {self._balance}"

class SavingsAccount(Account):
    def apply_interest(self):
        interest = self._balance * 0.05
        self._balance += interest
        print(f"Interest applied: {interest}. New balance: {self._balance}")

class CheckingAccount(Account):
    def issue_check(self, amount):
        self.withdraw(amount)

class Customer:
    def __init__(self, name, id_number):
        self.__name = name  # Private attribute
        self.__id_number = id_number  # Private attribute
        self.__accounts = []  # Private attribute

    def add_account(self, account):
        self.__accounts.append(account)

    def get_accounts(self):
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
        print(f"Auditing Account: {account}")

    @classmethod
    def create_customer(cls, name, id_number):
        return Customer(name, id_number)



def get_customer(customers, id_number):
    customer = customers.get(id_number)
    if not customer:
        print("Customer not found.")
        return None
    return customer

def get_account(customer, account_number):
    account = customer.get_account_by_number(account_number)
    if not account:
        print("Account not found.")
        return None
    return account


def handle_account_operations(account):
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Return to Main Menu")

        customer_choice = input("\nEnter choice: ")

        if customer_choice == "1":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                account.deposit(amount)
            else:
                print("Invalid amount.")
        elif customer_choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                account.withdraw(amount)
            else:
                print("Invalid amount.")
        elif customer_choice == "3":
            print(account)
        elif customer_choice == "4":
            break
        else:
            print("Invalid choice.")




def handle_create_customer(customers):
    name = input("Enter customer name: ")
    id_number = input("Enter ID number: ")
    customer = ManagerBanker.create_customer(name, id_number)
    customers[id_number] = customer
    print(f"Customer created: {customer}")



def handle_create_account(customers):
    id_number = input("Enter customer ID number: ")
    customer = get_customer(customers, id_number)
    if customer:
        account_type = input("Enter account type (savings/checking): ")
        if account_type.lower() not in ["savings", "checking"]:
            print("Invalid account type.")
            return

        account_number = input("Enter account number: ")
        if customer.get_account_by_number(account_number):
            print("An account with this number already exists for this customer.")
            return

        initial_balance = float(input("Enter initial balance: "))

        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, customer, initial_balance)
        else:
            account = CheckingAccount(account_number, customer, initial_balance)

        customer.add_account(account)
        print(f"Account created: {account}")


def handle_manager_operations(customers):
    while True:
        print("\nManager Menu")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Return to Main Menu")

        manager_choice = input("\nEnter choice: ")

        if manager_choice == "1":
            handle_create_customer(customers)
        elif manager_choice == "2":
            handle_create_account(customers)
        elif manager_choice == "3":
            break
        else:
            print("Invalid choice.")


def handle_customer_operations(customers):
    id_number = input("Enter customer ID number: ")
    customer = get_customer(customers, id_number)
    if customer:
        account_number = input("Enter account number: ")
        account = get_account(customer, account_number)
        if account:
            handle_account_operations(account)

def main():
    manager = ManagerBanker()
    customers = {}

    while True:
        print("\nBanking Application Main Menu")
        print("1. Manager Menu")
        print("2. Customer Menu")
        print("3. Exit")

        main_choice = input("\nEnter choice: ")

        if main_choice == "1":
            handle_manager_operations(customers)
        elif main_choice == "2":
            handle_customer_operations(customers)
        elif main_choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()



