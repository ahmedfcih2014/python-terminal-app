class BankAccount:
    def __init__(self, ba_id, ba_pass):
        self.__id = ba_id
        self.__pass = ba_pass
        self.__balance = 0

    def set_id(self, ba_id):
        self.__id = ba_id

    def get_id(self):
        return self.__id

    def set_pass(self, ba_pass):
        self.__pass = ba_pass

    def get_pass(self):
        return self.__pass

    def withdraw(self, amount: float) -> bool:
        if self.__balance - amount < 0:
            return False
        self.__balance -= amount
        return True

    def deposit(self, amount: float) -> bool:
        self.__balance += amount
        return True

    def get_balance(self):
        return self.__balance

    def delete_account(self):
        print("Balance will be removed:", self.__balance)
