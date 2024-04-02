class BankAccount:
    def __init__(self, balance = 0) -> None:
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} has been deposited into your account!\nYour balance is now ${self.balance}."
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} has been withdrawn from your account!\nYour balance is now ${self.balance}."
        else:
            return f"You have insufficient funds! You have ${amount} left."
    
    def see_balance(self):
        return f"Your balance is ${self.balance}"
    
    def quit(self):
        exit()
    
user_1 = BankAccount()

def ui():
    while True:
        print("Choose an option:\n1 | Deposit\n2 | Withdrawal\n3 | See balance\n4 | Quit")
        user_option = int(input("Option: "))
        
        if user_option == 1:
            deposit_amount = int(input("Enter your deposit amount: $"))
            print(user_1.deposit(deposit_amount))
        
        elif user_option == 2:
            withdrawal_amount = int(input("Enter your withdrawal amount ($50, $100, $200, or $500): $"))
            if withdrawal_amount not in [50, 100, 200, 500]:
                print("Withdrawal amount must be $50, $100, $200, or $500!")
            else:
                print(user_1.withdraw(withdrawal_amount))
            
        elif user_option == 3:
            print(user_1.see_balance())
            
        elif user_option == 4:
            print("Quitting...")
            user_1.quit()
            
ui()