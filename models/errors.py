"Error Models"


class GenericError(Exception):
    "Generic Error"

    def __init__(self, message: str = ""):
        class_name = self.__class__.__name__
        self.message = f"[{class_name}] {message}" if message else f"[{class_name}]"
        super().__init__(self.message)


class ConfigError(GenericError):
    "Config Error"

    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class LoginError(GenericError):
    "Login Error"

    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class WebDriverError(GenericError):
    "Web Driver Error"

    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class JinjaError(GenericError):
    "Jinja Error"

    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)
