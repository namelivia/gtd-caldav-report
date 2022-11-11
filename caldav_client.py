import caldav
import os


def get_calendars():
    client = caldav.DAVClient(
        url=os.environ.get("CALDAV_URL"),
        username=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD"),
    )
    return client.principal().calendars()
