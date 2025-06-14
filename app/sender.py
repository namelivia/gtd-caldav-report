from notifications.notifications import Notifications


def send_section(section):
    content = ""
    content += "---------------------\n"
    content += f"{section.title}\n"
    content += "---------------------\n"
    for item in section.items:
        content += f"{item}\n"
    content += "====================\n"
    Notifications.send(content)
