from .Date import Date
from .Creator import Creator
from .Organizer import Organizer
from .Attendee import Attendee
from .Reminder import Reminder
from typing import List, Optional


class Event(object):
    _kind: str                      # String
    _etag: str                      # String
    _id: str                        # String
    _status: str                    # String
    _html_link: str                 # String
    _created: Date                  # Date
    _updated: Date                  # Date
    _summary: str                   # String
    _description: str               # String
    _location: str                  # String
    _creator: Creator               # Creator
    _organizer: Organizer           # Organizer
    _start: Date                    # Date
    _end: Date                      # Date
    _recurring_event_id: str        # String
    _original_start_time: Date      # Date
    _transparency: str              # String
    _iCalUID: str                   # String
    _sequence: int                  # int
    _attendees: List[Attendee]      # array(Attendee)
    _guestsCanSeeOtherGuests: bool  # boolean
    _reminders: List[Reminder]      # Reminders

    def __init__(
        self,
        kind: str,
        etag: str,
        Id: str,
        status: str,
        htmlLink: str,
        created: Date,
        updated: Date,
        summary: str,
        description: str,
        location: str,
        creator: Creator,
        organizer: Organizer,
        start: Date,
        end: Date,
        recurringEventId: str,
        originalStartTime: Date,
        transparency: str,
        iCalUID: str,
        attendees: List[Attendee],
        guestsCanSeeOtherGuests: bool,
        reminders: List[Reminder]
    ):
        self._kind = kind
        self._etag = etag
        self._id = Id
        self._status = status
        self._html_link = htmlLink
        self._created = created
        self._updated = updated
        self._summary = summary
        self._description = description
        self._location = location
        self._creator = creator
        self._organizer = organizer
        self._start = start
        self._end = end
        self._recurring_event_id = recurringEventId
        self._original_start_time = originalStartTime
        self._transparency =transparency
        self._iCalUID = iCalUID
        self._attendees = attendees
        self._guestsCanSeeOtherGuests = guestsCanSeeOtherGuests
        self._reminders = reminders

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value

    @property
    def etag(self):
        return self._etag

    @etag.setter
    def etag(self, value):
        self._etag = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def htmlLink(self):
        return self._html_link

    @htmlLink.setter
    def htmlLink(self, value):
        self._html_link = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, value):
        self._updated = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def recurringEventId(self):
        return self._recurring_event_id

    @recurringEventId.setter
    def recurringEventId(self, value):
        self._recurring_event_id = value

    @property
    def originalStartTime(self):
        return self._original_start_time

    @originalStartTime.setter
    def originalStartTime(self, value):
        self._original_start_time = value

    @property
    def transparency(self):
        return self._transparency

    @transparency.setter
    def transparency(self, value):
        self._transparency = value

    @property
    def iCalUID(self):
        return self._iCalUID

    @iCalUID.setter
    def iCalUID(self, value):
        self._iCalUID = value

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def attendees(self):
        return self._attendees

    @attendees.setter
    def attendees(self, value):
        self._attendees = value

    @property
    def guestsCanSeeOtherGuests(self):
        return self._guestsCanSeeOtherGuests

    @guestsCanSeeOtherGuests.setter
    def guestsCanSeeOtherGuests(self, value):
        self._guestsCanSeeOtherGuests = value

    @property
    def reminders(self):
        return self._reminders

    @reminders.setter
    def reminders(self, value):
        self._reminders = value
