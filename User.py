import abc


class User:
    def __init__(self, name, u_id):
        # Define protected attributes :D
        self._id = str(u_id)
        self._name = str(name)
        self._password = None
        self._type = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_id(self, uid):
        self._id = uid

    def get_id(self):
        return self._id

    def set_password(self, password):
        self._password = str(password)

    def get_password(self):
        return self._password

    def set_type(self, u_type):
        self._type = str(u_type)

    def get_type(self):
        return self._type

    def login(self, uid, upass):
        # todo: need to change this implementation to use DB
        if self._id == uid and self._password == upass:
            return True
        return False

    @abc.abstractmethod
    def show_options(self):
        pass

    @abc.abstractmethod
    def handle_options(self, option):
        pass
