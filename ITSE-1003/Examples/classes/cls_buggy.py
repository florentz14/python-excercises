class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        # Error: solo aplica si amount > 0. CheckingAccount.monthly_update() llama
        # deposit(-self.fee); los cargos negativos nunca se aplican (el saldo no baja).
        if amount > 0:
            self.__balance += amount
            print(amount, "deposited.")

    def show_balance(self):
        print("Balance:", self.__balance)

    def monthly_update(self):
        print("General account update")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def monthly_update(self):
        # Error (name mangling): en una subclase, self.__balance no es el saldo del padre.
        # Se resuelve como _SavingsAccount__balance (inexistente), no como _BankAccount__balance.
        # Suele provocar AttributeError al calcular el interés.
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        print("Savings interest added.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def monthly_update(self):
        self.deposit(-self.fee)
        print("Checking account fee charged.")


account1 = SavingsAccount("Maria", 1000, 0.05)
account2 = CheckingAccount("John", 800, 20)
accounts = [account1, account2]
for account in accounts:
    account.monthly_update()
    account.show_balance()
# Error: __balance es “privado” por mangling; desde fuera de la clase no existe el atributo
# account1.__balance (AttributeError). Hay que usar un accesor público o show_balance().
print(account1.__balance)
