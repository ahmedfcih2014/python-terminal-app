from User import User
from Admin import Admin
from Customer import Customer

# for using shared variables
import variables
variables.init()


def create_account(_user: User):
    variables.users.append(_user)


def get_user_data(_type):
    _uname = input("Enter your name: ")
    _uid = input("Enter your id: ")
    _upass = input("Enter your pass: ")

    if _type == "Admin":
        u = Admin(_uname, _uid)
        u.set_password(_upass)
    else:
        u = Customer(_uname, _uid)
        u.set_password(_upass)

    return u


# todo, this function implementation must be changed to be more secure & accurate & must use DB
def login(_uid, _upass) -> User:
    for u in variables.users:
        if u.login(_uid, _upass):
            return u
    raise Exception("Wrong credentials")


try:
    print(variables.welcome_message)
    while True:
        option = input("Select an option: ")
        if option == "1":
            user = get_user_data("Admin")
            create_account(user)
        elif option == "2":
            user = get_user_data("Customer")
            create_account(user)
        elif option == "3":
            uid = input("Enter your ID: ")
            upass = input("Enter your Pass: ")
            _user = login(uid, upass)
            _user.show_options()
        else:
            raise Exception("Wrong option run me again")
except KeyboardInterrupt:
    print("Thanks for using ATM, Good Bye")
    exit(1)
except Exception as e:
    print(str(e))
    exit(1)
