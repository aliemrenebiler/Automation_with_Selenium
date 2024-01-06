"Account Credentials Model"

# pylint: disable=too-few-public-methods


class AccountCredentials:
    "Account Credentials Model Class"

    def __init__(
        self,
        username: str,
        password: str,
    ):
        self.username = username
        self.password = password
