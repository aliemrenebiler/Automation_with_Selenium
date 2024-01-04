"Account Credentials Model"

# pylint: disable=too-few-public-methods


class AccountCredentials:
    "Account Credentials Model Class"

    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password
