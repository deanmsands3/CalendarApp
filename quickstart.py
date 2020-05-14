import datetime
from ServiceBuilder import ServiceBuilder
from EventLister import EventLister


def main():
    """Shows basic usage of the Google Calendar API.
    """
    service_builder = ServiceBuilder()
    service = service_builder.build()
    # Call the Calendar API
    event_lister = EventLister(service)
    event_lister.list_events()


if __name__ == '__main__':
    main()
