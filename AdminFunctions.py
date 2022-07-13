from Customer import Customer
import variables


def customer_list():
    for u in variables.users:
        if u.get_type() == variables.user_types["customer"]:
            u.info()


def append_customer():
    uname = input("Enter customer name: ")
    upass = input("Enter customer pass: ")
    uid = input(variables.messages["customer_id"])
    cust = Customer(uname, uid)
    cust.set_password(upass)
    variables.users.append(cust)


def edit_customer():
    uid = input(variables.messages["customer_id"])
    field = input("Enter 1 for edit name or 2 for edit password: ")
    value = input("Enter field value for update: ")
    if str(field) not in ["1", "2"]:
        print("Wrong field number")
        return
    _accounts = []
    for u in variables.users:
        if u.get_type() == variables.user_types["customer"] and u.get_id() == uid:
            if str(field) == "1":
                u.set_name(value)
            else:
                u.set_password(value)
        _accounts.append(u)
    variables.users = _accounts


def delete_customer():
    uid = input(variables.messages["customer_id"])
    _accounts = []
    for u in variables.users:
        if str(u.get_id()) != str(uid):
            _accounts.append(u)
    variables.users = _accounts


def customer_deposit():
    customer_bank_account_action("deposit")


def customer_withdraw():
    customer_bank_account_action("withdraw")


def customer_inquiry():
    customer_bank_account_action("inquiry")


def customer_create_bank_account():
    customer_bank_account_action("create_bank_account")


def customer_bank_account_action(action):
    uid = input(variables.messages["customer_id"])
    for u in variables.users:
        if u.get_type() == variables.user_types["customer"] and str(u.get_id()) == str(uid):
            u.handle_options(variables.customer_options[action])
