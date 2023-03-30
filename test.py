from sender import send_section
from report_builder import build_report
from caldav_client import get_calendars
from gtd_framework import get_todos

# Retrieve the calendars from CalDav
calendars = get_calendars()

# Get the GTD Framework tasks
todos = get_todos(calendars)

# Build the report
report = build_report(todos)

# Print the report in the screen
if len(report) > 0:
    [send_section(section) for section in report]
else:
    send_section("No tasks to report")
