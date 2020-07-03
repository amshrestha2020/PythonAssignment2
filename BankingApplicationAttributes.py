'Imagine you are designing a banking application.'
'What would a customer look like?'
'What attributes would she have?'
'What methods would she have?'

class BankCustomer:
    """A bank account that has a non-negative balance."""
     # currency = "NPR"

    "CONSTRUCTOR"
    def __init__(self):
        self.balance = 0
        print("Welcome To Our Bank")
        account_number = int(input("Enter your bank account number :"))
        print("Your bank account number is :", account_number)
        account_holder_name = input("Enter full name :")
        print("The account holder full name is :", account_holder_name)

    "METHODS"
    def deposit(self):
        """Increase the account balance by amount and return the new balance."""
        amount = float(input("Enter an amount to be deposited :"))
        self.balance = self.balance + amount
        print("Amount Deposited :", amount)


    def withdraw(self):
        """Withdraw amount from the bank account, ensuring there are sufficient funds."""
        amount = float(input("Enter an amount to be withdrawn :"))
        if amount > self.balance:
            self.balance = self.balance - amount
            print("You Withdrew :", amount)
        else:
            print("Insufficient balance.")



    # def __str__(self):
    #     res = "*** Account Information ***\n"
    #     res += "Account ID :" + str(self.account_number) + "\n"
    #     res += "Customer :" + self.customer + "\n"
    #     res += "Balance :" + str(self.balance) + "\n"
    #     return res

"creating an object of class"
x = BankCustomer()

"Calling functions with that class object"
x.deposit()
x.withdraw()
