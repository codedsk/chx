# exceptions

class ChxException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class LocatorException(ChxException):
    pass


class TimeoutException(ChxException):
    pass

