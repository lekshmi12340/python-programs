class BankAccounts:
    def __init__(self):
        self.balance = 0
        self.name="XYZ"
        self.accountnumber=123456789
        print("Hello!!! ", self.name," welcome to  Bank Account" ,"your account number is",self.accountnumber)

    def deposits(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdrawn(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You can Withdraw:", amount)
        else:
            print("\n Sorry  withdraw amount violates the minimum balance condition ")

    def displayinfo(self):
        print("\n Total Available Balance for", self.name,"with account number",self.accountnumber,"is",self.balance)




# object creation
s = BankAccounts()

# Calling functions with that class object
s.deposits()
s.withdrawn()
s.displayinfo()
