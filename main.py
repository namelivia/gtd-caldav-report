from sender import send_section
from report_builder import build_report
from caldav_client import get_calendars
from gtd_framework import get_todos

import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Starting the script")

# Retrieve the calendars from CalDav
logger.info("Fetching calendars")
calendars = get_calendars()

# Get the GTD Framework tasks
logger.info("Fetching TODOs from calendars")
todos = get_todos(calendars)

# Build the report
logger.info("Building report")
report = build_report(todos)

# Print the report in the screen
if len(report) > 0:
    logger.info("Sending report")
    [send_section(section) for section in report]
else:
    logger.info("No tasks to report")
    send_section("No tasks to report")
