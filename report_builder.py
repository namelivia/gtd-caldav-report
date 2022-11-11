import datetime


class ReportSection:
    def __init__(self, title, items):
        self.title = title
        self.items = items


def _build_report_sections(todos, ranges, actions):
    sections = []
    for list_name, list_items in todos.items():
        for range_name, range_timestamp in ranges.items():
            for action_name, get_action in actions.items():
                item_names = [todo.name for todo in list_items if get_action(todo) is not None and get_action(todo) > range_timestamp]
                if len(item_names) > 0:
                    sections.append(
                        ReportSection(f"{list_name} taks {action_name} {range_name}:", item_names)
                    )
    return sections


def build_report(todos):
    # Ranges for which the report will be generated
    ranges = {
        # Currently I'm only interested in a weekly report
        "in the last 7 days": datetime.datetime.now() - datetime.timedelta(days=7),
        # "in the last 30 days": datetime.datetime.now() - datetime.timedelta(days=30),
        # "in the last 90 days": datetime.datetime.now() - datetime.timedelta(days=90),
        # "in the last 365 days": datetime.datetime.now() - datetime.timedelta(days=365),
    }

    # Actions for which the report will be generated
    actions = {
        # Currently I'm only interested in created and completed tasks
        "created": lambda x: x.created_at,
        "completed": lambda x: x.completed_at,
    }

    return _build_report_sections(todos, ranges, actions)
