from datetime import date as DateType, datetime as DateTimeType
from typing import Optional

class Date(object):
    _date: DateType
    _date_time: DateTimeType

    def __init__(self, date: Optional[DateType] = None, dateTime:Optional[DateTimeType] = None):
        self._date_time = dateTime
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def dateTime(self):
        return self._date_time

    @dateTime.setter
    def dateTime(self, value):
        self._date_time = value


    @property
    def DATE(self):
        date = self._date_time or self._date
        return date

    @DATE.setter
    def DATE(self, value):
        if isinstance(value, str):
            self._date_time = DateTimeType.fromisoformat(value)
        elif isinstance(value, DateType):
            self._date_time = DateTimeType(year=value.year, month=value.month, day=value.day)
        elif isinstance(value, DateTimeType):
            timestamp = value.timestamp()
            self._date_time = DateTimeType.utcfromtimestamp(timestamp)
        self._date = self._date_time.date()
