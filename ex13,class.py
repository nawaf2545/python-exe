class Customers:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def getBalance(self):
        return self.balance
if __name__ == '__main__':
    customer1 = Customers("Nawaf",7500)
while True:

    options = int(input("Enter your choice\n1- press #1 for deposit\n2- press #2 for withdraw\n3- press #3 for check balance\n4- press #4 for exite\nyour choice: "))

    if options == 1:
        deposit_amount = float(input("Enter deposit amount: "))
        current_balance = customer1.deposit(deposit_amount)
        print("The current balance is: ",current_balance)

    elif options ==2:
        withdraw_amount = float(input("Enter withdraw amount: "))
        current_balance = customer1.getBalance()
        if withdraw_amount >= 0:

            if current_balance >= withdraw_amount:
               new_balance = customer1.withdraw(withdraw_amount)
               print("the current balance is: ",new_balance)
            else:
                print("amount not correct")

        else:
            print("the amount must be greater or equal zero")
    elif options == 3:
        current_balance = customer1.getBalance()

        print("The balance is: ", current_balance)
    elif options == 0:
        break
    else:
        print("enter correct choice")