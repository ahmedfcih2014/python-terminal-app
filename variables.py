# for shared users' data structure til using database
def init():
    global users
    users = []


customer_options = {
    "create_bank_account": "1",
    "delete_bank_account": "2",
    "deposit": "3",
    "withdraw": "4",
    "inquiry": "5",
}


admin_options = {
    "customer_list": "0",
    "add_customer": "1",
    "edit_customer": "2",
    "delete_customer": "3",
    "create_bank_account": "4",
    "deposit": "5",
    "withdraw": "6",
    "inquiry": "7",
}


user_types = {
    "admin": "Admin",
    "customer": "Customer"
}


messages = {
    "customer_id": "Enter Customer ID: ",
    "bank_id": "Enter Bank Account ID: ",
    "bank_pass": "Enter Bank Account Pass: ",
    "amount": "Enter Amount: ",
    "acc_created": "Account created",
    "acc_deleted": "Account deleted",
    "amount_deposited": "Amount deposited successfully, Balance:",
    "amount_withdrawn": "Amount withdrawn successfully, Balance:",
}


customer_option_msg = """
Select an Option
1- Add Bank Account
2- Delete Bank Account
3- Deposit
4- Withdraw
5- Inquiry
"""


admin_option_msg = """
Select an Option
0- Customers List
1- Add Customer
2- Edit Customer
3- Delete Customer
4- Create Bank Account
5- Deposit
6- Withdraw
7- Inquiry
"""

welcome_message = """
****************************
* welcome to ATM system :D *
****************************
please choose an option:
1- create Admin account
2- create Customer account
3- login
for exit ctrl+c
"""
