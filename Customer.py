from User import User
from BankAccount import BankAccount
import variables


class Customer(User):
    def __init__(self, name, uid):
        User.__init__(self, name, uid)
        self.set_type(variables.user_types["customer"])
        self.__accounts = []

    def info(self):
        print("Name:", self._name, "| ID:", self._id)

    def show_options(self):
        try:
            while True:
                _option = input(variables.customer_option_msg)
                self.handle_options(_option)
        except Exception as e:
            raise e

    # todo
    def handle_options(self, option):
        if str(option) == variables.customer_options["create_bank_account"]:
            ba_id = input(variables.messages["bank_id"])
            ba_pass = input(variables.messages["bank_pass"])
            self.__accounts.append(BankAccount(ba_id, ba_pass))
            print(variables.messages["acc_created"])
        elif str(option) == variables.customer_options["delete_bank_account"]:
            ba_id = input(variables.messages["bank_id"])
            _accounts = []
            for a in self.__accounts:
                if a.get_id() != ba_id:
                    _accounts.append(a)
                else:
                    a.delete_account()
            self.__accounts = _accounts
            print(variables.messages["acc_deleted"])
        elif str(option) == variables.customer_options["deposit"]:
            ba_id = input(variables.messages["bank_id"])
            ba_pass = input(variables.messages["bank_pass"])
            amount = input(variables.messages["amount"])
            for a in self.__accounts:
                if a.get_id() == ba_id and a.get_pass() == ba_pass:
                    a.deposit(float(amount))
                    print(variables.messages["amount_deposited"], a.get_balance())
        elif str(option) == variables.customer_options["withdraw"]:
            ba_id = input(variables.messages["bank_id"])
            ba_pass = input(variables.messages["bank_pass"])
            amount = input(variables.messages["amount"])
            for a in self.__accounts:
                if a.get_id() == ba_id and a.get_pass() == ba_pass:
                    if a.withdraw(float(amount)):
                        print(variables.messages["amount_withdrawn"], a.get_balance())
        elif str(option) == variables.customer_options["inquiry"]:
            ba_id = input(variables.messages["bank_id"])
            for a in self.__accounts:
                if a.get_id() == ba_id:
                    print("Balance is:", a.get_balance())
