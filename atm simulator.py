class ATM:
    def _init_(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Invalid amount or insufficient balance"

def run_atm():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM!")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        option = input("Choose an option: ")

        if option == '1':
            print(f"Your current balance is: {atm.check_balance()}")
        elif option == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        elif option == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))
        elif option == '4':
            print("Thanks for using the ATM!")
            break
        else:
            print("Invalid option. Please try again.")

run_atm()