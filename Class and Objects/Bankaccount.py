
class BankAccount:
    def __init__(self):
        self.balance = 10

    def deposit(self,amount):
        self.balance =+ amount

    def _withdraw(self,amount):
        self.balance -=amount

    def __show_balance(self):
        print("Balance of bank account - > ", self.balance)

    def isAuth_true(self,isAuth):
        if isAuth:
            print("You are auth")
            self.__show_balance()

        else:
            print("No authe, no bal")

    def isWithdrawl_true(self,isWithdraw,amount):
        if isWithdraw:
            print("You are auth, withdraw")
            self._withdraw(amount)

        else:
            print("No Auth, No bal")

acc = BankAccount()
acc.deposit(1000)
acc.isWithdrawl_true(True,500)
acc.isAuth_true(True)





