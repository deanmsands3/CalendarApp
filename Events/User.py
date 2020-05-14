class User(object):
    _display_name: str
    _email: str

    def __init__(self, email: str, displayName: str):
        self._email = email
        self._display_name = displayName

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def displayName(self) -> str:
        return self._display_name

    @displayName.setter
    def displayName(self, value: str) -> None:
        self._display_name = value

