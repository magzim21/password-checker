import re
# Insert a banner


class PasswordCheck:
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    Cudos to the author of original function https://stackoverflow.com/a/32542964/11103492 
    """

    def __init__(self, password: str) -> object:
        self._password = password

        # calculating the length
        self._length_error = len(self._password) < 8

        # searching for digits
        self._digit_error = re.search(r"\d", self._password) is None

        # searching for uppercase
        self._uppercase_error = re.search(r"[A-Z]", self._password) is None

        # searching for lowercase
        self._lowercase_error = re.search(r"[a-z]", self._password) is None

        # searching for symbols
        self._symbol_error = re.search(
            r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', self._password) is None

        # overall result
        self._password_ok = not (
            self._length_error or self._digit_error or self._uppercase_error or self._lowercase_error or self._symbol_error)

    @property
    def password(self):
        return self._password

    @property
    def length_error(self):
        return self._length_error

    @property
    def digit_error(self):
        return self._digit_error

    @property
    def uppercase_error(self):
        return self._uppercase_error

    @property
    def lowercase_error(self):
        return self._lowercase_error

    @property
    def symbol_error(self):
        return self._symbol_error

    @property
    def password_ok(self):
        return self._password_ok




if __name__ == "__main__":
    PasswordCheck("example$Password")
    
