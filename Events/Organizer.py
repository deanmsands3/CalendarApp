from .User import User


class Organizer(User):
    def __init__(self, email: str, displayName: str):
        User.__init__(self, email, displayName)
