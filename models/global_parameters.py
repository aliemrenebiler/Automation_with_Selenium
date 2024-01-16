"Global Parameters Model"

# pylint: disable=too-few-public-methods


class GlobalParameters:
    "Global Parameters Model Class"

    def __init__(
        self,
        timeout: int = None,
        login_timeout: int = None,
        page_load_time: int = None,
    ):
        self.timeout = timeout
        self.login_timeout = login_timeout
        self.page_load_time = page_load_time
