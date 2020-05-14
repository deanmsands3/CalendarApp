import datetime


class Event(object):
    def __init__(self, name="", description="", start=None, end=None, *args, **kwargs):
        self._category = 0
        self._name = name
        self._description = description
        self._start = start or datetime.datetime.now()
        self._end = start or datetime.datetime.now()

