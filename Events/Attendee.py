from .User import User


class Attendee(User):
    response_status: str

    def __init__(self, email: str, displayName: str, responseStatus: str):
        User.__init__(self, email, displayName)
        self._response_status = responseStatus

    @property
    def responseStatus(self):
        return self._response_status

    @responseStatus.setter
    def responseStatus(self, value):
        self._response_status = value
