from googleapiclient.discovery import Resource
import datetime


class EventLister(object):
    def __init__(self, service: Resource):
        self._service = service

    def get_events(self, *args, **kwargs):
        events = self._service.events()
        events_list = events.list(*args, **kwargs).execute()
        return events_list

    def list_events(self) -> None:
        """
            Prints the start and name of the next 10 events on the user's calendar.
        """
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_list = self.get_events(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        )

        events = events_list.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        for event in events:
            self.list_event(event)

    @staticmethod
    def list_event(event: dict) -> None:
        start_entry = event['start']
        # A stupidly confusing way of checking for either an entry named "dateTime" first or else simply "date"
        start = start_entry.get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

