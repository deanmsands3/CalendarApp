class Override(object):
    _method: str	# String
    _minutes: int	# int

    def __init__(self, method: str, minutes: int):
        self._method = method
        self._minutes = minutes

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._minutes = value
