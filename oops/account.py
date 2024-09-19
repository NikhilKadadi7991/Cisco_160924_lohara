class Account:
    def __init__(self, number, name, minimum_bal = 1000):
        self.__number = number
        self.__name = name
        self.__balance = minimum_bal

    def __repr__(self):
        return f'[number = {self.__number}, name = {self.__name}, balance={self.__balance}]'
    
    def __str__(self):
        return self.__repr__()
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        self.__balance-=amount

        '''if amount > self._balance:
            print('No enough balance')
            return
        self._balance -= amount'''
    
Girish_ac = Account(name='Girish',number='9999999999999', minimum_bal=280000)
print(Girish_ac)

Girish_ac.deposit(1)
print(Girish_ac)

Girish_ac.withdraw(86000)
print(Girish_ac)