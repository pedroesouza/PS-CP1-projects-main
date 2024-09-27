#Pedro Souza, Comments
class BankAccount: #Bank account class
    def __init__(self, account_number, balance=0): #Initialize the variables
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #Adds money to balance
        if amount > 0: #Checks if the amount is 0, if it is, do nothing
            self.balance += amount #Adds amount
            return True #Bool returns
        return False

    def withdraw(self, amount): #Withdraws from bank account
        if 0 < amount <= self.balance: #Checks if your balance has enough for the withdraw
            self.balance -= amount #Removes amount
            return True #Bool returns
        return False

    def get_balance(self): #Returns your balance
        return self.balance

def create_account(): #Account creator, enters account number and initial balance
    account_number = input("Enter account number: ") #Asks 2 questions
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance) #Returns answers

def main(): #Interface that asks you what you want to do with your bank account
    accounts = {} #Create array of accounts
    while True:
        print("\n1. Create Account") #Prints the 5 options of what to do.
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") #Asks the user to write which option they want.
        
        if choice == '1': #If they chose create account, run the create account function and print when it is created succesfully.
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #If the choice is 2, 3, or 4 ask for account number and then run the iff statements in the bottom 
            account_number = input("Enter account number: ")
            if account_number in accounts: #If the number exists in the accounts
                account = accounts[account_number]
                if choice == '2': #If they chose 2, ask for deposit amount
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount): #Checks if deposite amount is valid, prints success
                        print(f"Deposited ${amount:.2f} successfully!")
                    else: #If amount invalid, print that amount is invalid
                        print("Invalid deposit amount.")
                elif choice == '3': #If they chose 2, ask for withdraw amount
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount): #Checks if withdraw amount is valid, prnt sucess
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else: #If amount invalid, say that they have insufficient funds
                        print("Invalid withdrawal amount or insufficient funds.")
                else: #If they chose 4, print account balance.
                    print(f"Current balance: ${account.get_balance():.2f}")
            else: #If account number invalid, print that it isnt found
                print("Account not found.")
        
        elif choice == '5': #If hey chose 5, thank them, and exit
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else: #If they didn't chose from 1-5, say that it is invalid and ask them to try again.
            print("Invalid choice. Please try again.")

if __name__ == "__main__": #Run main
    main()