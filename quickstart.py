import datetime
from ServiceBuilder import ServiceBuilder
from EventLister import EventLister
import NewEvents

def main():
    """Shows basic usage of the Google Calendar API.
    """
    service_builder = ServiceBuilder()
    service = service_builder.build()

    # Call the Calendar API
    #breakpoint()

    event_lister = EventLister(service)
    event_lister.list_events()
    service.events().insert(NewEvents)

if __name__ == '__main__':
    main()
