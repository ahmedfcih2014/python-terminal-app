import variables
from User import User
import AdminFunctions


class Admin(User):
    def __init__(self, name, uid):
        User.__init__(self, name, uid)
        self.set_type(variables.user_types["admin"])

    def show_options(self):
        try:
            while True:
                _option = input(variables.admin_option_msg)
                self.handle_options(_option)
        except Exception as e:
            raise e

    # todo
    def handle_options(self, option):
        if str(option) == variables.admin_options["customer_list"]:
            AdminFunctions.customer_list()
        elif str(option) == variables.admin_options["add_customer"]:
            AdminFunctions.append_customer()
        elif str(option) == variables.admin_options["edit_customer"]:
            AdminFunctions.edit_customer()
        elif str(option) == variables.admin_options["delete_customer"]:
            AdminFunctions.delete_customer()
        elif str(option) == variables.admin_options["deposit"]:
            AdminFunctions.customer_deposit()
        elif str(option) == variables.admin_options["withdraw"]:
            AdminFunctions.customer_withdraw()
        elif str(option) == variables.admin_options["inquiry"]:
            AdminFunctions.customer_inquiry()
        elif str(option) == variables.admin_options["create_bank_account"]:
            AdminFunctions.customer_create_bank_account()
